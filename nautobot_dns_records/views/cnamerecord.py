"""Views for the cname record model"""

from nautobot.core.views import generic

from nautobot_dns_records import models
from nautobot_dns_records import tables


class CnameRecordsListView(generic.ObjectListView):
    """List all CName Records."""

    queryset = models.CNameRecord.objects.all()
    table = tables.CnameRecordTable


class CnameRecordView(generic.ObjectView):
    """Show a Address Record"""

    queryset = models.CNameRecord.objects.all()
