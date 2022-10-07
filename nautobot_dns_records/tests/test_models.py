"""Tests for the nautobot_dns_records models."""

import django.db.models.fields
from django.core.exceptions import ValidationError
from nautobot.utilities.testing import TestCase
from nautobot.ipam.models import IPAddress
from nautobot.dcim.models import Device

from nautobot_dns_records.models import Record, AddressRecord, CNameRecord, TxtRecord, LocRecord, PtrRecord, SshfpRecord
from nautobot_dns_records.tests.helpers import (
    random_valid_dns_ttl,
    random_valid_dns_name,
    random_ipv4_address,
    random_ipv6_address,
)
from nautobot_dns_records.tests.mixins import AbstractModelMixinTestCase


class RecordTestCase(AbstractModelMixinTestCase):
    """Test the Record model."""

    mixin = Record

    def setUp(self):
        self.device = Device(name="test-device")

    def test_record_is_abstract(self):
        with self.assertRaisesMessage(TypeError, "Abstract models cannot be instantiated."):
            Record(label=random_valid_dns_name(), ttl=random_valid_dns_ttl())

    def test_record_has_label(self):
        self.assertIsInstance(Record._meta.get_field("label"), django.db.models.fields.CharField)

    def test_record_single_label_to_long(self):
        label = "thisisaveryveryveryverylongdnslabelwhichisinvalid12345678942424"
        with self.assertRaisesMessage(ValidationError, f"The label {label} is longer than allowed (> 63)"):
            record = self.model(label=f"{label}.test", ttl=1)
            record.clean_fields()

    def test_record_to_long(self):
        label = "thisisaveryveryveryverylongdnslabelwhichisinvalid123456789424.thisisaveryveryveryverylongdnslabelwhichisinvalid123456789424.thisisaveryveryveryverylongdnslabelwhichisinvalid123456789424.thisisaveryveryveryverylongdnslabelwhichisinvalid123456789424.test1234"
        with self.assertRaisesMessage(ValidationError, "Ensure this value has at most 255 characters (it has 256)."):
            record = self.model(label=label, ttl=1)
            record.clean_fields()

    def test_record_has_ttl(self):
        self.assertIsInstance(Record._meta.get_field("ttl"), django.db.models.fields.IntegerField)

    def test_record_ttl_validation(self):
        with self.assertRaisesMessage(ValidationError, "Ensure this value is greater than or equal to 1."):
            record = self.model(label=random_valid_dns_name(), ttl=0)
            record.clean_fields()
        with self.assertRaisesMessage(ValidationError, "Ensure this value is less than or equal to 604800."):
            record.ttl = 604801
            record.clean_fields()
        record.ttl = 10
        record.clean_fields()

    def test_record_idna_encoding(self):
        record = self.model(label="💩.test", ttl=1)
        record.save()
        self.assertEqual(record.label, "xn--ls8h.test")

    def test_str(self):
        record = self.model(label=random_valid_dns_name(), ttl=1)
        record.save()
        self.assertEqual(record.__str__(), record.label)

    def test_device_assignment(self):
        record = self.model(label=random_valid_dns_name(), ttl=1, device=self.device)
        self.assertEqual(record.device, self.device)

class AddressRecordTestCase(TestCase):
    """Test the AddressRecord Model"""

    def setUp(self):
        self.test_ipv4 = IPAddress(address=random_ipv4_address())
        self.test_ipv6 = IPAddress(address=random_ipv6_address())

    def test_record_creation_ipv4(self):
        record_v4 = AddressRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), address=self.test_ipv4)
        self.assertEqual(record_v4.address, self.test_ipv4)

    def test_record_creation_ipv6(self):
        record_v6 = AddressRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), address=self.test_ipv6)
        self.assertEqual(record_v6.address, self.test_ipv6)


class CNameRecordTestCase(TestCase):
    """Test the CNameRecord Model"""

    def test_record_creation(self):
        target = random_valid_dns_name()
        record = CNameRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), target=target)
        self.assertEqual(record.target, target)

    def test_record_target_encoding(self):
        record = CNameRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), target="💩.test")
        record.save()
        self.assertEqual(record.target, "xn--ls8h.test")


class TxtRecordTestCase(TestCase):
    """Test the TxtRecord Model"""

    def test_txt_record_creation(self):
        value = "This is a test!"
        record = TxtRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), value=value)
        self.assertEqual(record.value, value)


class LocRecordTestCase(TestCase):
    """Test the LocRecord Model"""

    def test_loc_record_creation(self):
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        record.save()
        self.assertEqual(record.label, "big.ben.hm")

    def test_loc_record_field_validation_degLat(self):  # pylint: disable=C0103
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'degLat': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.degLat = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'degLat': ['Ensure this value is less than or equal to 90.']}"
        ):
            record.degLat = 91
            record.clean_fields()

    def test_loc_record_field_validation_degLong(self):  # pylint: disable=C0103
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'degLong': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.degLong = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'degLong': ['Ensure this value is less than or equal to 180.']}"
        ):
            record.degLong = 181
            record.clean_fields()

    def test_loc_record_field_validation_minLat(self):  # pylint: disable=C0103
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'minLat': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.minLat = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'minLat': ['Ensure this value is less than or equal to 59.']}"
        ):
            record.minLat = 60
            record.clean_fields()

    def test_loc_record_field_validation_minLong(self):  # pylint: disable=C0103
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'minLong': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.minLong = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'minLong': ['Ensure this value is less than or equal to 59.']}"
        ):
            record.minLong = 60
            record.clean_fields()

    def test_loc_record_field_validation_secLat(self):  # pylint: disable=C0103
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'secLat': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.secLat = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'secLat': ['Ensure this value is less than or equal to 59.999.']}"
        ):
            record.secLat = 60
            record.clean_fields()

    def test_loc_record_field_validation_secLong(self):  # pylint: disable=C0103
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'secLong': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.secLong = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'secLong': ['Ensure this value is less than or equal to 59.999.']}"
        ):
            record.secLong = 60
            record.clean_fields()

    def test_loc_record_field_validation_altitude(self):
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'altitude': ['Ensure this value is greater than or equal to -100000.']}"
        ):
            record.altitude = -100001
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'altitude': ['Ensure this value is less than or equal to 42849672.95.']}"
        ):
            record.altitude = 42849672.96
            record.clean_fields()

    def test_loc_record_field_validation_precision(self):
        record = LocRecord(
            label="big.ben.hm",
            ttl=random_valid_dns_ttl(),
            degLong=73,
            minLong=30,
            secLong=43,
            dirLong="E",
            degLat=53,
            minLat=6,
            secLat=1,
            dirLat="S",
            altitude=517,
            precision=0,
        )
        with self.assertRaisesMessage(
            ValidationError, "{'precision': ['Ensure this value is greater than or equal to 0.']}"
        ):
            record.precision = -1
            record.clean_fields()
        with self.assertRaisesMessage(
            ValidationError, "{'precision': ['Ensure this value is less than or equal to 90000000.0.']}"
        ):
            record.precision = 90000000.01
            record.clean_fields()


class PtrRecordTestCase(TestCase):
    """Test the PtrRecord Model."""

    def setUp(self):
        self.test_ipv4 = IPAddress(address=random_ipv4_address())
        self.test_ipv6 = IPAddress(address=random_ipv6_address())

    def test_ptr_record_creation_ipv4(self):
        record = PtrRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), address=self.test_ipv4)
        self.assertEqual(record.address, self.test_ipv4)

    def test_ptr_record_creation_ipv6(self):
        record = PtrRecord(label=random_valid_dns_name(), ttl=random_valid_dns_ttl(), address=self.test_ipv6)
        self.assertEqual(record.address, self.test_ipv6)


class SshfpRecordTestCase(TestCase):
    """Test the SSHFP Record Model."""

    def test_sshfp_record_creation(self):
        record = SshfpRecord(
            label=random_valid_dns_name(),
            ttl=random_valid_dns_ttl(),
            algorithm=1,
            hashType=1,
            fingerprint="81bc1331bcd5b1c605a142d36af7720afd6b38c9",
        )
        self.assertEqual(record.fingerprint, "81bc1331bcd5b1c605a142d36af7720afd6b38c9")

    def test_sshfp_record_validation(self):
        with self.assertRaisesMessage(ValidationError, "{'fingerprint': ['Not a valid fingerprint in hex format']}"):
            record = SshfpRecord(
                label=random_valid_dns_name(),
                ttl=random_valid_dns_ttl(),
                algorithm=1,
                hashType=1,
                fingerprint="81bc1331bcd5b1c605a142d36af7720afdx6b38c9",
            )
            record.clean_fields()
