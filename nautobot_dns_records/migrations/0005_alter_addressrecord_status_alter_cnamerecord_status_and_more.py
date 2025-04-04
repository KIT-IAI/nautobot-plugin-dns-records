# Generated by Django 4.2.18 on 2025-03-21 11:43

from django.db import migrations
import django.db.models.deletion
import nautobot.extras.models.statuses


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0122_add_graphqlquery_owner_content_type"),
        ("nautobot_dns_records", "0004_auto_20250108_0728"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addressrecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="cnamerecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="locrecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="ptrrecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="srvrecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="sshfprecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
        migrations.AlterField(
            model_name="txtrecord",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="%(app_label)s_%(class)s_related",
                to="extras.status",
            ),
        ),
    ]
