from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Product, User, Customer


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "image", "price", "manufacturer", "description", "active",
                    "category"]
    list_filter = ["category", "manufacturer"]
    search_fields = ["name", "price", "description", "category__name"]
    readonly_fields = ["product_image"]

    def product_image(self, product):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='120px'/>".format(img_url=product.image.name, alt=product.name))


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Customer)
