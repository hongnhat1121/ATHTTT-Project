from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    image = SerializerMethodField()

    def get_image(self, product):
        request = self.context['request']
        name = product.image.name
        if name.startswith("static/"):
            path = '/%s' % name
        else:
            path = '/static/%s' % name

        return request.build_absolute_uri(path)

    class Meta:
        model = Product
        fields = ["id", "name", "image", "price", "category"]

class ProductDetailSerializer(ProductSerializer):
    class Meta:
        model = ProductSerializer.Meta.model
        fields = ProductSerializer.Meta.fields + ["manufacturer", "description"]