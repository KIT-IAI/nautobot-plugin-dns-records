"""Urls for nautobot_dns_records."""

from django.urls import path

from nautobot_dns_records import views

urlpatterns = [
    path("address_records/", views.AddressRecordsListView.as_view(), name="address_records_list"),
    path("txt_records/", views.TxtRecordsListView.as_view(), name="txt_records_list"),
    path("loc_records/", views.LocRecordsListView.as_view(), name="loc_records_list"),
    path("cname_records/", views.CnameRecordsListView.as_view(), name="cname_records_list"),
    path("ptr_records/", views.PtrRecordsListView.as_view(), name="ptr_records_list"),
    path("sshfp_records/", views.SshfpRecordsListView.as_view(), name="sshfp_records_list"),
]
