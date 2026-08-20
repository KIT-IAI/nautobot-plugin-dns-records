"""Tests for DNS record API serializers."""

from django.contrib.contenttypes.models import ContentType
from django.test import RequestFactory, override_settings
from nautobot.apps.testing import TestCase
from nautobot.extras.models import Status
from nautobot.ipam.models import IPAddress

from nautobot_dns_records.api.serializers import (
    AddressRecordSerializer,
    CNameRecordSerializer,
    PtrRecordSerializer,
)
from nautobot_dns_records.models import AddressRecord, CNameRecord, PtrRecord


@override_settings(ALLOWED_HOSTS=["localhost"])
class SerializerTestCase(TestCase):
    """Test API serializer input and output."""

    def setUp(self):
        self.status = Status.objects.get(name="Active")
        self.status.content_types.add(ContentType.objects.get_for_model(CNameRecord))
        self.ipAddress = IPAddress.objects.filter(ip_version="4").first()
        self.request = RequestFactory().get("/", HTTP_HOST="localhost")

    def serialize(self, serializer_class, instance):
        """Serialize an instance with a request context."""
        return serializer_class(instance, context={"request": self.request}).data

    def test_address_record_serializer_contains_expected_fields(self):
        record = AddressRecord.objects.create(
            label="www.example.test",
            ttl=3600,
            address=self.ipAddress,
            status=self.status,
        )

        data = self.serialize(AddressRecordSerializer, record)

        self.assertEqual(data["label"], "www.example.test")
        self.assertEqual(data["ttl"], 3600)
        self.assertIn("address", data)
        self.assertIn("status", data)

    def test_cname_serializer_validates_required_target(self):
        serializer = CNameRecordSerializer(
            data={
                "label": "alias.example.test",
                "ttl": 3600,
                "target": "target.example.test",
                "status": self.status.pk,
            }
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_ptr_serializer_exposes_computed_reverse_label(self):
        address_record = AddressRecord.objects.create(
            label="www.example.test",
            ttl=3600,
            address=self.ipAddress,
            status=self.status,
        )
        record = PtrRecord.objects.create(
            ttl=3600,
            address=self.ipAddress,
            record=address_record,
            status=self.status,
        )

        data = self.serialize(PtrRecordSerializer, record)

        self.assertEqual(data["label"], record.label)
