"""API urls for nautobot_dns_records."""

from rest_framework import routers
from nautobot_dns_records.api.views import AddressRecordViewSet, CNameRecordViewSet

router = routers.DefaultRouter()
router.register("address-records", AddressRecordViewSet, basename="address-records")
router.register(r"cname-records", CNameRecordViewSet, basename="cname-records")
urlpatterns = router.urls
