"""Views for the sshfp record model"""

from nautobot.core.views import generic

from nautobot_dns_records import models
from nautobot_dns_records import tables


class SshfpRecordsListView(generic.ObjectListView):
    """List all SSHFP Records."""

    queryset = models.SshfpRecord.objects.all()
    table = tables.GenericRecordTable
