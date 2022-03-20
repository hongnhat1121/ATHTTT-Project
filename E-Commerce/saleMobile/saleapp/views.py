from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Category, Product
from .serializes import CategorySerializer, ProductSerializer, ProductDetailSerializer
from .paginator import BasePagination
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    pagination_class = BasePagination

    def get_queryset(self):
        products = Product.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None:
            products = products.filter(name__icontains=q)

        cate_id = self.request.query_params.get('category_id')
        if cate_id is not None:
            products = products.filter(category_id=cate_id)

        return products
