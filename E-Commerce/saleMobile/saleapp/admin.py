from django.contrib import admin
from django.contrib.auth.models import Permission
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import Category, Customer, Product, HashTag, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Product
        fields = '__all__'


class ProductTagInline(admin.TabularInline):
    pass


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ["id", "name", "price", "manufacturer", "active", "category"]
    search_fields = ["name", "manufacturer", "category__name"]
    list_filter = ["manufacturer", "category__name"]
    readonly_fields = ["images"]

    def images(self, product):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='200px'/>".
                         format(img_url=product.image.name, alt=product.name))

    class Media:
        css = {
            'all': ('/static/css/home.css',)
        }


class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "phone_number"]
    search_fields = ["full_name", "phone_number"]


class SaleAppAdminSite(admin.AdminSite):
    site_header = 'HỆ THỐNG DỊCH VỤ THIẾT BỊ DI ĐỘNG'

    def get_urls(self):
        return [
                   path('sale-stats/', self.sale_stats)
               ] + super().get_urls()

    def sale_stats(self, request):
        product_count = Product.objects.count()
        stats = Category.objects.annotate(product_cou=Count('my_product')).values("id", "name", "product_cou")

        return TemplateResponse(request, 'admin/sale-stats.html', {
            'product_count': product_count,
            'stats': stats
        })


admin_site = SaleAppAdminSite('my_sale_app')

# admin.site.register(Category)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(User)
# admin.site.register(Permission)
#
admin_site.register(Category)
admin_site.register(Product, ProductAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(User)
