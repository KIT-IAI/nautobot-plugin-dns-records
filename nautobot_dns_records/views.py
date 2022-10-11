"""Views for nautobot_dns_records."""

from nautobot.core.views import generic

from nautobot_dns_records import models
from nautobot_dns_records import tables


class AddressRecordsListView(generic.ObjectListView):
    """List all Address Records."""

    queryset = models.AddressRecord.objects.all()
    table = tables.AddressRecordTable


class TxtRecordsListView(generic.ObjectListView):
    """List all TXT Records."""

    queryset = models.TxtRecord.objects.all()
    table = tables.GenericRecordTable


class LocRecordsListView(generic.ObjectListView):
    """List all LOC Records."""

    queryset = models.LocRecord.objects.all()
    table = tables.GenericRecordTable


class CnameRecordsListView(generic.ObjectListView):
    """List all CName Records."""

    queryset = models.CNameRecord.objects.all()
    table = tables.GenericRecordTable


class PtrRecordsListView(generic.ObjectListView):
    """List all PTR Records."""

    queryset = models.PtrRecord.objects.all()
    table = tables.GenericRecordTable


class SshfpRecordsListView(generic.ObjectListView):
    """List all SSHFP Records."""

    queryset = models.SshfpRecord.objects.all()
    table = tables.GenericRecordTable
