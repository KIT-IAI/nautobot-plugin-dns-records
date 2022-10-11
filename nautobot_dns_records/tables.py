"""Table Views for DNS Models."""

import django_tables2 as tables
from nautobot.extras.tables import StatusTableMixin
from nautobot.utilities.tables import BaseTable, ToggleColumn

from nautobot_dns_records import models


class AddressRecordTable(StatusTableMixin, BaseTable):
    """Table for all record based models."""

    pk = ToggleColumn()
    label = tables.Column(linkify=True)
    address = tables.Column(linkify=True)

    class Meta(BaseTable.Meta):
        model = models.AddressRecord
        fields = ("pk", "label", "address")


class GenericRecordTable(StatusTableMixin, BaseTable):
    """Table for all record based models."""

    pk = ToggleColumn()
    label = tables.Column(linkify=True)
    device = tables.Column(linkify=True)

    class Meta(BaseTable.Meta):
        model = models.AddressRecord
        fields = ("pk", "label", "device")
