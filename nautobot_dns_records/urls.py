"""Urls for nautobot_dns_records."""

from django.urls import path

from nautobot_dns_records.views import addressrecord, txtrecord, locrecord, cnamerecord, ptrrecord, sshfprecord

urlpatterns = [
    path("address_record/", addressrecord.AddressRecordsListView.as_view(), name="addressrecord_list"),
    path("address_record/add/", addressrecord.AddressRecordEditView.as_view(), name="addressrecord_add"),
    path("address_record/<uuid:pk>/", addressrecord.AddressRecordView.as_view(), name="addressrecord"),
    path("address_record/<uuid:pk>/edit/", addressrecord.AddressRecordEditView.as_view(), name="addressrecord_edit"),
    path("address_record/<uuid:pk>/delete/", addressrecord.AddressRecordDeleteView.as_view(), name="addressrecord_delete"),
    path("txt_record/", txtrecord.TxtRecordsListView.as_view(), name="txtrecord_list"),
    path("txt_record/<uuid:pk>/", txtrecord.TxtRecordView.as_view(), name="txtrecord"),
    path("loc_record/", locrecord.LocRecordsListView.as_view(), name="locrecord_list"),
    path("loc_record/<uuid:pk>/", locrecord.LocRecordView.as_view(), name="locrecord"),
    path("cname_record/", cnamerecord.CnameRecordsListView.as_view(), name="cnamerecord_list"),
    path("cname_record/<uuid:pk>/", cnamerecord.CnameRecordView.as_view(), name="cnamerecord"),
    path("ptr_record/", ptrrecord.PtrRecordsListView.as_view(), name="ptrrecord_list"),
    path("ptr_record/<uuid:pk>/", ptrrecord.PtrRecordView.as_view(), name="ptrrecord"),
    path("sshfp_record/", sshfprecord.SshfpRecordsListView.as_view(), name="sshfprecord_list"),
    path("sshfp_record/<uuid:pk>/", sshfprecord.SshfpRecordView.as_view(), name="sshfprecord"),
]
