"""API urls for nautobot_dns_records."""

from rest_framework import routers
from nautobot_dns_records.api.views import AddressRecordViewSet

router = routers.DefaultRouter()
router.register("address-records", AddressRecordViewSet, basename="address-records")
urlpatterns = router.urls
