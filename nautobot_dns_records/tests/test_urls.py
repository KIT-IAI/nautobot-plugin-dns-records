"""Tests for DNS record URL registration."""

from django.urls import reverse
from nautobot.apps.testing import TestCase


class UrlTestCase(TestCase):
    """Test that all public plugin routes are registered."""

    def test_list_routes_are_registered(self):
        route_names = (
            "addressrecord_list",
            "cnamerecord_list",
            "txtrecord_list",
            "locrecord_list",
            "ptrrecord_list",
            "sshfprecord_list",
            "srvrecord_list",
        )

        for route_name in route_names:
            with self.subTest(route_name=route_name):
                self.assertTrue(reverse(f"plugins:nautobot_dns_records:{route_name}"))

    def test_custom_tab_routes_are_registered(self):
        self.assertIn(
            "/plugins/dns/devices/",
            reverse(
                "plugins:nautobot_dns_records:device_records_tab",
                kwargs={"pk": "00000000-0000-0000-0000-000000000001"},
            ),
        )
        self.assertIn(
            "/plugins/dns/ip-addresses/",
            reverse(
                "plugins:nautobot_dns_records:address_records_tab",
                kwargs={"pk": "00000000-0000-0000-0000-000000000001"},
            ),
        )
