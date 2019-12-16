from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from .views import StockViewSet

router = routers.DefaultRouter()

router.register('stock', StockViewSet)


urlpatterns = [
    path('', include(router.urls)),
]