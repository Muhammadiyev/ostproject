from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base-auth/', include('rest_framework.urls')),
    path('', include('users.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('products.urls')),
    path('api/v1/', include('report.urls')),
    path('api/v1/', include('stock.urls')),
    path('auth/', include('djoser.urls')),
    path('auth_token/', include('djoser.urls.authtoken')),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)