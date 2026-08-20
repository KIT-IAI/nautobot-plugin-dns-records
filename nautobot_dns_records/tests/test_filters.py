"""Tests for DNS record filtersets."""

from nautobot.apps.testing import TestCase
from nautobot.extras.models import Status
from nautobot.ipam.models import IPAddress

from nautobot_dns_records.filters import (
    AddressRecordFilterSet,
    CNameRecordFilterSet,
    LocRecordFilterSet,
    PtrRecordFilterSet,
    SshfpRecordFilterSet,
    SrvRecordFilterSet,
    TxtRecordFilterSet,
)
from nautobot_dns_records.models import AddressRecord, CNameRecord, PtrRecord


class SearchFilterTestCase(TestCase):
    """Test global-search filters used by Nautobot."""

    def setUp(self):
        self.status = Status.objects.get(name="Active")
        self.ip_address = IPAddress.objects.filter(ip_version="4").first()
        self.address_record = AddressRecord.objects.create(
            label="www.example.test",
            ttl=3600,
            address=self.ip_address,
            status=self.status,
        )

    def test_all_record_filtersets_expose_q(self):
        filtersets = (
            AddressRecordFilterSet,
            CNameRecordFilterSet,
            TxtRecordFilterSet,
            LocRecordFilterSet,
            PtrRecordFilterSet,
            SshfpRecordFilterSet,
            SrvRecordFilterSet,
        )

        for filterset in filtersets:
            with self.subTest(filterset=filterset.__name__):
                self.assertIn("q", filterset.base_filters)

    def test_address_record_search_matches_label(self):
        results = AddressRecordFilterSet({"q": "www.example"}, queryset=AddressRecord.objects.all()).qs

        self.assertQuerySetEqual(results, [self.address_record], transform=lambda record: record)

    def test_cname_record_search_matches_target(self):
        record = CNameRecord.objects.create(
            label="alias.example.test",
            ttl=3600,
            target="target.example.test",
            status=self.status,
        )

        results = CNameRecordFilterSet({"q": "target.example"}, queryset=CNameRecord.objects.all()).qs

        self.assertQuerySetEqual(results, [record], transform=lambda item: item)

    def test_ptr_record_search_matches_address_record_label(self):
        ptr_record = PtrRecord.objects.create(
            ttl=3600,
            address=self.ip_address,
            record=self.address_record,
            status=self.status,
        )

        results = PtrRecordFilterSet({"q": "www.example"}, queryset=PtrRecord.objects.all()).qs

        self.assertQuerySetEqual(results, [ptr_record], transform=lambda item: item)
