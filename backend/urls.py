"""backend URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from shopping.views import ShoppingItemViewSet

router = routers.DefaultRouter()
router.register(
    'shopping-item', ShoppingItemViewSet, basename='shopping-item'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
