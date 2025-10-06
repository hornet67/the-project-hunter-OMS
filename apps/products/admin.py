from django.contrib import admin
from .models import *


# -------------------------
# MainGroup Admin
# -------------------------
@admin.register(MainGroup)
class MainGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'added_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('status',)
    list_per_page = 20


# -------------------------
# Manufacturer Admin
# -------------------------
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_id', 'name', 'main_group', 'type', 'status', 'added_at', 'update_at')
    search_fields = ('name', 'type')
    list_filter = ('main_group', 'type', 'status', 'company_id')
    list_per_page = 20


# -------------------------
# Category Admin
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_group', 'type', 'company_id', 'status', 'added_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('main_group', 'status', 'type', 'company_id')
    list_per_page = 20


# -------------------------
# Forms Admin
# -------------------------
@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_group', 'type', 'company_id', 'status', 'added_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('main_group', 'status', 'type', 'company_id')
    list_per_page = 20


# -------------------------
# Units Admin
# -------------------------
@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name', 'main_group', 'type', 'company_id', 'status', 'added_at', 'update_at')
    search_fields = ('unit_name',)
    list_filter = ('main_group', 'status', 'type', 'company_id')
    list_per_page = 20


# -------------------------
# Product Admin
# -------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name', 'product_code', 'category', 'form', 'unit',
        'company_id', 'group', 'quantity', 'cp', 'mrp', 'status', 'added_at', 'update_at'
    )
    search_fields = ('product_name', 'product_code', 'group')
    list_filter = ('status', 'category', 'company_id', 'form', 'unit')
    list_per_page = 25

    # -------------------------
    # Dynamic ForeignKey Filtering
    # -------------------------
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Dynamically filters dropdown options to only show active (status=1) related entries.
        """
        from .models import Manufacturer, Category, Forms, Units
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(status=1)
        elif db_field.name == "form":
            kwargs["queryset"] = Forms.objects.filter(status=1)
        elif db_field.name == "unit":
            kwargs["queryset"] = Units.objects.filter(status=1)
        elif db_field.name == "company_id":
            kwargs["queryset"] = Manufacturer.objects.filter(status=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
