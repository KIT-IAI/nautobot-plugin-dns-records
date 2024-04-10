# Generated by Django 3.2.25 on 2024-04-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nautobot_dns_records', '0002_status'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='addressrecord',
            constraint=models.UniqueConstraint(fields=('label', 'address'), name='arec_unique_label_address_combination'),
        ),
        migrations.AddConstraint(
            model_name='cnamerecord',
            constraint=models.UniqueConstraint(fields=('label',), name='unique_label'),
        ),
        migrations.AddConstraint(
            model_name='locrecord',
            constraint=models.UniqueConstraint(fields=('label',), name='loc_unique_label'),
        ),
        migrations.AddConstraint(
            model_name='ptrrecord',
            constraint=models.UniqueConstraint(fields=('label', 'address'), name='ptr_unique_label_address'),
        ),
        migrations.AddConstraint(
            model_name='txtrecord',
            constraint=models.UniqueConstraint(fields=('label', 'value'), name='txt_unique_label_value_combination'),
        ),
    ]
