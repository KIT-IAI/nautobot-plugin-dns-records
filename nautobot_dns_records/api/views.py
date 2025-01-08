# pylint: disable=too-many-ancestors
"""API views for nautobot_dns_records."""
from nautobot.apps.api import NautobotModelViewSet

from nautobot_dns_records.models import AddressRecord, CNameRecord, TxtRecord
from nautobot_dns_records.api.serializers import AddressRecordSerializer, CNameRecordSerializer, TxtRecordSerializer


class AddressRecordViewSet(NautobotModelViewSet):
    """API viewset for interacting with AddressRecord objects."""

    queryset = AddressRecord.objects.all()
    serializer_class = AddressRecordSerializer


class CNameRecordViewSet(NautobotModelViewSet):
    """API viewset for interacting with CNameRecord objects."""

    queryset = CNameRecord.objects.all()
    serializer_class = CNameRecordSerializer

class TxtRecordViewSet(NautobotModelViewSet):
    """API viewset for interacting with TxtRecord objects."""

    queryset = TxtRecord.objects.all()
    serializer_class = TxtRecordSerializer
