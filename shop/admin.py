from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'total_quantity', 'remaining_quantity']
    list_filter = ['available', 'created', 'updated']
    search_fields = ['name']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
