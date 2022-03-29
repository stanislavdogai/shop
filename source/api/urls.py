from django.urls import path, include

from rest_framework import routers

from api import views


product_routers = routers.DefaultRouter()
product_routers.register(r'product', views.ProductViewSet)

router = routers.DefaultRouter()
router.register(r'orders', views.OrderViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(product_routers.urls)),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]