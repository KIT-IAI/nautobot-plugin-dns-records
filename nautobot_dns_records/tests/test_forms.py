"""Tests for DNS record forms."""

from nautobot.apps.testing import TestCase
from nautobot.extras.models import Status

from nautobot_dns_records.forms import (
    AddressRecordFilterForm,
    CnameRecordForm,
    CNameRecordFilterForm,
    PtrRecordForm,
    PtrRecordFilterForm,
    SrvRecordFilterForm,
    TxtRecordFilterForm,
)


class RecordFormTestCase(TestCase):
    """Test DNS record create and filter forms."""

    def setUp(self):
        self.status = Status.objects.get(name="Active")

    def test_cname_form_rejects_invalid_target(self):
        form = CnameRecordForm(
            data={
                "label": "alias.example.test",
                "ttl": 3600,
                "target": "target..example.test",
                "status": self.status.pk,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("target", form.errors)

    def test_ptr_form_requires_address_and_record(self):
        form = PtrRecordForm(data={"ttl": 3600, "status": self.status.pk})

        self.assertFalse(form.is_valid())
        self.assertIn("address", form.errors)
        self.assertIn("record", form.errors)

    def test_filter_forms_expose_search_field(self):
        filter_forms = (
            AddressRecordFilterForm,
            CNameRecordFilterForm,
            PtrRecordFilterForm,
            SrvRecordFilterForm,
            TxtRecordFilterForm,
        )

        for filter_form in filter_forms:
            with self.subTest(filter_form=filter_form.__name__):
                self.assertIn("q", filter_form.base_fields)  # pylint: disable=no-member
