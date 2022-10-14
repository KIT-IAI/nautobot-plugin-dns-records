import nautobot.ipam.models
from django import forms
from nautobot.extras.forms import RelationshipModelFormMixin
from nautobot.utilities.forms import BootstrapMixin, DynamicModelChoiceField

from nautobot_dns_records import models


class AddressRecordForm(BootstrapMixin, RelationshipModelFormMixin, forms.ModelForm):
    """Address Record create/edit form"""

    address = DynamicModelChoiceField(queryset=nautobot.ipam.models.IPAddress.objects.all())

    class Meta:
        model = models.AddressRecord
        fields = ["label", "ttl", "address", "status", "tags"]
