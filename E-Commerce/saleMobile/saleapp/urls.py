from django.contrib import admin
from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework import routers


router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, 'category')
router.register("products", views.ProductViewSet, 'product')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls)
]