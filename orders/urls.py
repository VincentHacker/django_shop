from rest_framework.routers import DefaultRouter

from .views import OrderViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet, basename = 'orders')

# всегда должна быть переменная urlpatterns, otherwise it won't work
urlpatterns = router.urls