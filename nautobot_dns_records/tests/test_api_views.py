"""Tests for DNS record API viewsets."""

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.test import override_settings
from nautobot.apps.testing import TestCase
from nautobot.extras.models import Status
from nautobot.ipam.models import IPAddress
from nautobot.users.models import Token
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
            *Permission.objects.filter(
                content_type=ContentType.objects.get_for_model(AddressRecord),
                codename__in=(
                    "add_addressrecord",
                    "change_addressrecord",
                    "delete_addressrecord",
                    "view_addressrecord",
                ),
            )
        )
        cls.token = Token.objects.create(user=cls.user, write_enabled=True)
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

    def test_list_rejects_anonymous_request(self):
        request = APIRequestFactory().get("/api/plugins/dns/address-records/")
        response = AddressRecordViewSet.as_view({"get": "list"})(request)

        self.assertIn(response.status_code, (401, 403))

    def test_create_update_and_delete_record_with_write_token(self):
        headers = {"HTTP_AUTHORIZATION": f"Token {self.token.key}"}
        payload = {
            "label": "created.example.test",
            "ttl": 3600,
            "address": self.record.address.pk,
            "status": self.status.pk,
        }
        request = APIRequestFactory().post("/api/plugins/dns/address-records/", payload, format="json", **headers)
        response = AddressRecordViewSet.as_view({"post": "create"})(request)

        self.assertEqual(response.status_code, 201, response.data)
        created_record = AddressRecord.objects.get(label=payload["label"])
        self.assertEqual(created_record.ttl, payload["ttl"])

        request = APIRequestFactory().patch(
            f"/api/plugins/dns/address-records/{created_record.pk}/",
            {"ttl": 7200},
            format="json",
            **headers,
        )
        response = AddressRecordViewSet.as_view({"patch": "partial_update"})(request, pk=created_record.pk)

        self.assertEqual(response.status_code, 200, response.data)
        created_record.refresh_from_db()
        self.assertEqual(created_record.ttl, 7200)

        request = APIRequestFactory().delete(f"/api/plugins/dns/address-records/{created_record.pk}/", **headers)
        response = AddressRecordViewSet.as_view({"delete": "destroy"})(request, pk=created_record.pk)

        self.assertEqual(response.status_code, 204, response.data)
        self.assertFalse(AddressRecord.objects.filter(pk=created_record.pk).exists())
