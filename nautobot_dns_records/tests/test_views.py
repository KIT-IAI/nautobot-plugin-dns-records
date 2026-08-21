"""Tests for DNS record UI views."""

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import override_settings
from django.urls import reverse
from nautobot.apps.testing import TestCase
from nautobot.extras.models import Status
from nautobot.ipam.models import IPAddress

from nautobot_dns_records.models import AddressRecord


class AddressRecordViewTestCase(TestCase):
    """Test authenticated and anonymous access to address record views."""

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_superuser(
            username="dns-ui-admin",
            email="dns-ui-admin@example.test",
            password="test-password",
        )
        cls.status = Status.objects.get(name="Active")
        cls.status.content_types.add(ContentType.objects.get_for_model(AddressRecord))
        cls.record = AddressRecord.objects.create(
            label="ui.example.test",
            ttl=3600,
            address=IPAddress.objects.filter(ip_version="4").first(),
            status=cls.status,
        )

    def test_anonymous_user_is_redirected_from_list(self):
        response = self.client.get(reverse("plugins:nautobot_dns_records:addressrecord_list"))

        self.assertIn(response.status_code, (302, 403))

    @override_settings(EXEMPT_VIEW_PERMISSIONS=["*"])
    def test_authenticated_user_can_view_list_and_detail(self):
        self.client.force_login(self.user)

        list_response = self.client.get(reverse("plugins:nautobot_dns_records:addressrecord_list"))
        detail_response = self.client.get(
            reverse("plugins:nautobot_dns_records:addressrecord", kwargs={"pk": self.record.pk})
        )

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(detail_response.status_code, 200)
