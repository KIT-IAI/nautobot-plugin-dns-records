"""Urls for nautobot_dns_records."""

from django.urls import path

from nautobot_dns_records.views import addressrecord, txtrecord, locrecord, cnamerecord, ptrrecord, sshfprecord

urlpatterns = [
    path("address_record/", addressrecord.AddressRecordsListView.as_view(), name="address_records_list"),
    path("address_record/add/", addressrecord.AddressRecordEditView.as_view(), name="addressrecord_add"),
    path("address_record/<uuid:pk>/edit", addressrecord.AddressRecordEditView.as_view(), name="addressrecord_edit"),
    path("address_record/<uuid:pk>/", addressrecord.AddressRecordView.as_view(), name="address_record"),
    path("txt_record/", txtrecord.TxtRecordsListView.as_view(), name="txt_records_list"),
    path("txt_record/<uuid:pk>/", txtrecord.TxtRecordView.as_view(), name="txt_record"),
    path("loc_record/", locrecord.LocRecordsListView.as_view(), name="loc_records_list"),
    path("loc_record/<uuid:pk>/", locrecord.LocRecordView.as_view(), name="loc_record"),
    path("cname_record/", cnamerecord.CnameRecordsListView.as_view(), name="cname_records_list"),
    path("cname_record/<uuid:pk>/", cnamerecord.CnameRecordView.as_view(), name="cname_record"),
    path("ptr_record/", ptrrecord.PtrRecordsListView.as_view(), name="ptr_records_list"),
    path("ptr_record/<uuid:pk>/", ptrrecord.PtrRecordView.as_view(), name="ptr_record"),
    path("sshfp_record/", sshfprecord.SshfpRecordsListView.as_view(), name="sshfp_records_list"),
    path("sshfp_record/<uuid:pk>/", sshfprecord.SshfpRecordView.as_view(), name="sshfp_record"),
]
