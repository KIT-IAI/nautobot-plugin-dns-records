# Generated by Django 3.2.18 on 2023-02-28 08:08

from django.db import migrations


def create_status(apps, schema_editor):
    """Create initial status objects"""

    statuses = ["Active", "Staged", "Decommissioned"]
    content_type = apps.get_model("contenttypes.ContentType")
    for i in statuses:
        status = apps.get_model("extras.Status").objects.get(name=i)
        for model in apps.app_configs["nautobot_dns_records"].get_models():
            if hasattr(model, "status"):
                ct = content_type.objects.get_for_model(model)
                status.content_types.add(ct)


def reverse_create_status(apps, schema_editor):
    """Reverse adding dns models to status content_types."""

    statuses = ["Active", "Staged", "Decommissioned"]
    content_type = apps.get_model("contenttypes.ContentType")
    for i in statuses:
        status = apps.get_model("extras.Status").objects.get(name=i)
        for model in apps.app_configs["nautobot_dns_records"].get_models():
            if hasattr(model, "status"):
                ct = content_type.objects.get_for_model(model)
                status.content_types.remove(ct)


class Migration(migrations.Migration):
    dependencies = [
        ("nautobot_dns_records", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(code=create_status, reverse_code=reverse_create_status),
    ]
