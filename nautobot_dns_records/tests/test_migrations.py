"""Tests for DNS record migrations."""

import ipaddress

from django.test import tag
from django_test_migrations.migrator import Migrator
from nautobot.apps.testing import TestCase


@tag("migration_test")
class PtrRecordMigrationTestCase(TestCase):
    """Test the reversible PTR record migration."""

    migrate_from = ("nautobot_dns_records", "0005_alter_addressrecord_status_alter_cnamerecord_status_and_more")
    migrate_to = ("nautobot_dns_records", "0006_remove_ptrrecord_ptr_unique_label_address_and_more")

    def setUp(self):
        self.migrator = Migrator(database="default")
        old_state = self.migrator.apply_initial_migration(self.migrate_from)
        self.apps = old_state.apps

    def tearDown(self):
        self.migrator.reset()
        super().tearDown()

    def test_ptr_record_migration_forward_and_backward(self):
        ip_address_model = self.apps.get_model("ipam", "IPAddress")
        status_model = self.apps.get_model("extras", "Status")
        address_record_model = self.apps.get_model("nautobot_dns_records", "AddressRecord")
        ptr_record_model = self.apps.get_model("nautobot_dns_records", "PtrRecord")

        status = status_model.objects.get(name="Active")
        ptr_record_model.objects.all().delete()
        address_record_model.objects.all().delete()
        address = ip_address_model.objects.create(
            host="192.0.2.1",
            mask_length=32,
            type="host",
            status=status,
            ip_version=4,
            dns_name="",
            description="",
        )
        address_record = address_record_model.objects.create(
            label="migration-target.example.test",
            ttl=3600,
            address=address,
            status=status,
        )
        ptr_record = ptr_record_model.objects.create(
            label=ipaddress.ip_address(address.host).reverse_pointer,
            ttl=3600,
            address=address,
            status=status,
        )

        new_state = self.migrator.apply_tested_migration(self.migrate_to)
        migrated_record = new_state.apps.get_model("nautobot_dns_records", "PtrRecord").objects.get(pk=ptr_record.pk)
        self.assertEqual(migrated_record.record_id, address_record.pk)

        old_state = self.migrator.apply_tested_migration(self.migrate_from)
        rolled_back_record = old_state.apps.get_model("nautobot_dns_records", "PtrRecord").objects.get(pk=ptr_record.pk)
        self.assertEqual(rolled_back_record.label, ipaddress.ip_address(address.host).reverse_pointer)
