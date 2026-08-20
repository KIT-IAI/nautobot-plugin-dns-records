"""Nautobot DNS-Records filters."""

from nautobot.apps.filters import BaseFilterSet, SearchFilter

from nautobot_dns_records.models import (
    AddressRecord,
    CNameRecord,
    TxtRecord,
    LocRecord,
    PtrRecord,
    SshfpRecord,
    SrvRecord,
)


class AddressRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of Address records."""

    q = SearchFilter(filter_predicates={"label": "icontains", "address__address": "icontains"})

    class Meta:
        model = AddressRecord
        fields = ["label", "address", "device"]


class CNameRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of CName records."""

    q = SearchFilter(filter_predicates={"label": "icontains", "target": "icontains"})

    class Meta:
        model = CNameRecord
        fields = ["label", "target"]


class TxtRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of Txt records."""

    q = SearchFilter(filter_predicates={"label": "icontains", "value": "icontains"})

    class Meta:
        model = TxtRecord
        fields = [
            "label",
        ]


class LocRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of Location records."""

    q = SearchFilter(filter_predicates={"label": "icontains"})

    class Meta:
        model = LocRecord
        fields = [
            "label",
        ]


class PtrRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of Ptr records."""

    q = SearchFilter(
        filter_predicates={
            "address__address": "icontains",
            "record__label": "icontains",
        }
    )

    class Meta:
        model = PtrRecord
        fields = ["address", "record"]


class SshfpRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of Sshfp records."""

    q = SearchFilter(filter_predicates={"label": "icontains", "fingerprint": "icontains"})

    class Meta:
        model = SshfpRecord
        fields = ["label", "fingerprint"]


class SrvRecordFilterSet(BaseFilterSet):
    """FilterSet for filtering a set of Srv records."""

    q = SearchFilter(filter_predicates={"label": "icontains", "target": "icontains"})

    class Meta:
        model = SrvRecord
        fields = [
            "label",
        ]
