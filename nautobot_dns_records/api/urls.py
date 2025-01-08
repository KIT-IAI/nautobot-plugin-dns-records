"""API urls for nautobot_dns_records."""

from rest_framework import routers
from nautobot_dns_records.api.views import AddressRecordViewSet, CNameRecordViewSet,TxtRecordViewSet, LocRecordViewSet, PtrRecordViewSet, SshfpRecordViewSet

router = routers.DefaultRouter()
router.register("address-records", AddressRecordViewSet, basename="address-records")
router.register(r"cname-records", CNameRecordViewSet, basename="cname-records")
router.register("txt-records", TxtRecordViewSet, basename="txt-records")
router.register("loc-records", LocRecordViewSet, basename="loc-records")
router.register("ptr-records", PtrRecordViewSet, basename="ptr-records")
router.register("sshfp-records", SshfpRecordViewSet, basename="sshfp-records")
urlpatterns = router.urls
