from django.contrib import admin
from .models import Manufacturer, Category, Forms, Units, Product

# -------------------------
# Manufacturer
# -------------------------
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_name', 'name', 'type', 'status')
    search_fields = ('company_id', 'company_name', 'name', 'type')


# -------------------------
# Category
# -------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'type', 'company', 'status')
    list_filter = ('status',)
    search_fields = ('category_name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "type":
            # Show only manufacturers where type='manufa'
            kwargs["queryset"] = Manufacturer.objects.filter(type='manufa')
        elif db_field.name == "company":
            # Show only manufacturers where company_name='DHS'
            kwargs["queryset"] = Manufacturer.objects.filter(company_name='DHS')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



# -------------------------
# Forms
# -------------------------
@admin.register(Forms)
class FormsAdmin(admin.ModelAdmin):
    list_display = ('id', 'form_name', 'company_id', 'status', 'added_at', 'update_at')
    search_fields = ('form_name',)
    list_filter = ('status', 'company_id')


# -------------------------
# Units
# -------------------------
@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_name', 'company_id', 'status', 'added_at', 'update_at')
    search_fields = ('unit_name',)
    list_filter = ('status', 'company_id')


# -------------------------
# Product
# -------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_code', 'category', 'form', 'unit', 'company_id', 'quantity', 'cp', 'mrp', 'status', 'added_at', 'update_at')
    search_fields = ('product_name', 'product_code', 'group')
    list_filter = ('status', 'category', 'company_id', 'form', 'unit')
