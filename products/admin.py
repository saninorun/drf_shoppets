from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)
