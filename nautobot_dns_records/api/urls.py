"""API urls for nautobot_dns_records."""

from rest_framework import routers
from nautobot_dns_records.api.views import AddressRecordViewSet, CNameRecordViewSet,TxtRecordViewSet

router = routers.DefaultRouter()
router.register("address-records", AddressRecordViewSet, basename="address-records")
router.register(r"cname-records", CNameRecordViewSet, basename="cname-records")
router.register("txt-records", TxtRecordViewSet, basename="txt-records")
urlpatterns = router.urls
