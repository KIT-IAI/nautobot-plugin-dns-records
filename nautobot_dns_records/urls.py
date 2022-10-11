"""Urls for nautobot_dns_records."""

from django.urls import path

from nautobot_dns_records import views

urlpatterns = [
    path("address_record/", views.AddressRecordsListView.as_view(), name="address_records_list"),
    path("address_record/<uuid:pk>/", views.AddressRecordView.as_view(), name="address_record"),
    path("txt_record/", views.TxtRecordsListView.as_view(), name="txt_records_list"),
    path("txt_record/<uuid:pk>/", views.TxtRecordView.as_view(), name="txt_record"),
    path("loc_record/", views.LocRecordsListView.as_view(), name="loc_records_list"),
    path("cname_record/", views.CnameRecordsListView.as_view(), name="cname_records_list"),
    path("ptr_record/", views.PtrRecordsListView.as_view(), name="ptr_records_list"),
    path("sshfp_record/", views.SshfpRecordsListView.as_view(), name="sshfp_records_list"),
]
