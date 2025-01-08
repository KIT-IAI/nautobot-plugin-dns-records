# pylint: disable=too-many-ancestors
"""API views for nautobot_dns_records."""
from nautobot.apps.api import NautobotModelViewSet

from nautobot_dns_records.models import AddressRecord
from nautobot_dns_records.api.serializers import AddressRecordSerializer


class AddressRecordViewSet(NautobotModelViewSet):
    """API viewset for interacting with AddressRecord objects."""

    queryset = AddressRecord.objects.all()
    serializer_class = AddressRecordSerializer
