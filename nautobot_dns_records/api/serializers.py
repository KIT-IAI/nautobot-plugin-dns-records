# pylint: disable=too-many-ancestors
"""Model serializers for nautobot_dns_records."""

from nautobot.apps.api import NautobotModelSerializer

from nautobot_dns_records.models import AddressRecord


class AddressRecordSerializer(NautobotModelSerializer):
    """API serializer for interacting with AddressRecord objects."""

    class Meta:
        model = AddressRecord
        fields = ("label", "ttl", "device", "address", "status")
