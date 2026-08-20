"""Tests for DNS record API viewsets."""

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.test import override_settings
from nautobot.apps.testing import TestCase
from nautobot.extras.models import Status
from nautobot.ipam.models import IPAddress
from rest_framework.test import APIRequestFactory, force_authenticate

from nautobot_dns_records.api.views import AddressRecordViewSet
from nautobot_dns_records.models import AddressRecord


@override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
class AddressRecordViewSetTestCase(TestCase):
    """Test authenticated API reads."""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_superuser(
            username="dns-api-admin",
            email="dns-api-admin@example.test",
            password="test-password",
        )
        cls.status = Status.objects.get(name="Active")
        cls.status.content_types.add(ContentType.objects.get_for_model(AddressRecord))
        cls.user.user_permissions.add(
            Permission.objects.get(
                codename="view_addressrecord",
                content_type=ContentType.objects.get_for_model(AddressRecord),
            )
        )
        cls.record = AddressRecord.objects.create(
            label="api.example.test",
            ttl=3600,
            address=IPAddress.objects.filter(ip_version="4").first(),
            status=cls.status,
        )

    def test_list_returns_address_records_for_authenticated_user(self):
        request = APIRequestFactory().get("/api/plugins/dns/address-records/")
        force_authenticate(request, user=self.user)
        response = AddressRecordViewSet.as_view({"get": "list"})(request)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["label"], self.record.label)

    def test_list_search_filter_returns_matching_record(self):
        request = APIRequestFactory().get("/api/plugins/dns/address-records/?q=api.example")
        force_authenticate(request, user=self.user)
        response = AddressRecordViewSet.as_view({"get": "list"})(request)

        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["label"], self.record.label)
