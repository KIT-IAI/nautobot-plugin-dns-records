"""Views for nautobot_dns_records."""

from nautobot.core.views import generic

from nautobot_dns_records import models
from nautobot_dns_records import tables


class LocRecordsListView(generic.ObjectListView):
    """List all LOC Records."""

    queryset = models.LocRecord.objects.all()
    table = tables.LocRecordTable


class LocRecordView(generic.ObjectView):
    """Show a Address Record"""

    queryset = models.LocRecord.objects.all()
