from django.contrib import admin
from .models import Product, Banner, ProductImage

# Register your models here.

admin.site.register(Banner)


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]


admin.site.register(Product, ProductAdmin)
