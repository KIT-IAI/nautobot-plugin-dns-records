"""Views for the loc record model"""

from nautobot.core.views import generic

from nautobot_dns_records import models
from nautobot_dns_records import tables


class TxtRecordsListView(generic.ObjectListView):
    """List all TXT Records."""

    queryset = models.TxtRecord.objects.all()
    table = tables.TxtRecordTable


class TxtRecordView(generic.ObjectView):
    """Show a Address Record"""

    queryset = models.TxtRecord.objects.all()
