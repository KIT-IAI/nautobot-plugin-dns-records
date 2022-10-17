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


class CnameRecordForm(BootstrapMixin, RelationshipModelFormMixin, forms.ModelForm):
    """CName Record create/edit form"""

    class Meta:
        model = models.CNameRecord
        fields = ["label", "ttl", "target", "status", "tags"]


class LocRecordForm(BootstrapMixin, RelationshipModelFormMixin, forms.ModelForm):
    """LOC Record create/edit form"""

    class Meta:
        model = models.LocRecord
        fields = [
            "label",
            "ttl",
            "degLat",
            "minLat",
            "secLat",
            "degLong",
            "minLong",
            "secLong",
            "precision",
            "altitude",
            "status",
            "tags",
        ]


class PtrRecordForm(BootstrapMixin, RelationshipModelFormMixin, forms.ModelForm):
    """PTR Record create/edit form"""

    address = DynamicModelChoiceField(queryset=nautobot.ipam.models.IPAddress.objects.all())

    class Meta:
        model = models.PtrRecord
        fields = ["label", "ttl", "address", "status", "tags"]


class SshfpRecordForm(BootstrapMixin, RelationshipModelFormMixin, forms.ModelForm):
    """SSHFP Record create/edit form"""

    class Meta:
        model = models.SshfpRecord
        fields = ["label", "ttl", "algorithm", "hashType", "fingerprint", "status", "tags"]


class TxtRecordForm(BootstrapMixin, RelationshipModelFormMixin, forms.ModelForm):
    """TXT Record create/edit form"""

    class Meta:
        model = models.TxtRecord
        fields = ["label", "ttl", "value", "status", "tags"]
