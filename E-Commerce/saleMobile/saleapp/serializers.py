from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "image", "price", "manufacturer", "category"]
