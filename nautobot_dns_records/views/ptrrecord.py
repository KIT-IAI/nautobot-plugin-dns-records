"""Views for the ptr record model"""

from nautobot.core.views import generic

from nautobot_dns_records import models
from nautobot_dns_records import tables


class PtrRecordsListView(generic.ObjectListView):
    """List all PTR Records."""

    queryset = models.PtrRecord.objects.all()
    table = tables.AddressRecordTable


class PtrRecordView(generic.ObjectView):
    """Show a Address Record"""

    queryset = models.PtrRecord.objects.all()
