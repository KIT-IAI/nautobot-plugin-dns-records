"""Views for the address record model"""

from nautobot.core.views import generic

from nautobot_dns_records import models, tables, forms


class AddressRecordsListView(generic.ObjectListView):
    """List all Address Records."""

    queryset = models.AddressRecord.objects.all()
    table = tables.AddressRecordTable


class AddressRecordView(generic.ObjectView):
    """Show a Address Record"""

    queryset = models.AddressRecord.objects.all()


class AddressRecordEditView(generic.ObjectEditView):
    """Edit an address record"""

    queryset = models.AddressRecord.objects.all()
    model_form = forms.AddressRecordForm
