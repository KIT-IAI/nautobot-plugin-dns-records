# pylint: disable=too-many-ancestors
"""Model serializers for nautobot_dns_records."""

from nautobot.apps.api import NautobotModelSerializer

from nautobot_dns_records.models import AddressRecord, CNameRecord, TxtRecord


class AddressRecordSerializer(NautobotModelSerializer):
    """API serializer for interacting with AddressRecord objects."""

    class Meta:
        model = AddressRecord
        fields = ("label", "ttl", "device", "address", "status")

class CNameRecordSerializer(NautobotModelSerializer):
    """API serializer for interacting with CNameRecord objects."""

    class Meta:
        model = CNameRecord
        fields = ("label", "ttl", "device", "target", "status")

class TxtRecordSerializer(NautobotModelSerializer):
    """API serializer for interacting with TxtRecord objects."""

    class Meta:
        model = TxtRecord
        fields = ("label", "ttl", "device", "value", "status")
