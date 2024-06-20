from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet,ProductGenericViewset

router = DefaultRouter()
router.register('products-atoz',ProductViewSet,basename='products')


urlpatterns = router.urls