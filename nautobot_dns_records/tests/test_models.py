"""Tests for the nautobot_dns_records models."""

import django.db.models.fields
from django.core.exceptions import ValidationError

from nautobot_dns_records.models import Record
from nautobot_dns_records.tests.helpers import random_valid_dns_ttl, random_valid_dns_name
from nautobot_dns_records.tests.mixins import AbstractModelMixinTestCase


class RecordTestCase(AbstractModelMixinTestCase):
    """Test the Record model."""

    mixin = Record

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
