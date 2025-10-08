from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect, get_object_or_404
from .models import *

# -------------------------
# Custom User model
# -------------------------
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'age', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active')


# -------------------------
# Company Type
# -------------------------
@admin.register(CompanyType)
class CompanyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# -------------------------
# Company Info
# -------------------------
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('company_id', 'company_name', 'email', 'phone_number', 'type', 'domain', 'is_active','activated_by','activated_at')
    search_fields = ('company_name', 'email', 'domain')
    list_filter = ('type', 'is_active')


@admin.register(PendingCompany)
class PendingCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'email', 'phone_number', 'type', 'activate_button', 'delete_button')
    search_fields = ('company_name', 'email')
    list_filter = ('type',)

    # Activate button
    def activate_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Activate</a>',
            f'activate/{obj.id}/'  # changed company_id → id
        )
    activate_button.short_description = 'Activate Company'

    # Delete button
    def delete_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Delete</a>',
            f'delete/{obj.id}/'  # changed company_id → id
        )
    delete_button.short_description = 'Delete Company'

    # Custom URLs
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('activate/<int:pending_company_id>/', self.admin_site.admin_view(self.activate_company), name='activate-company'),
            path('delete/<int:pending_company_id>/', self.admin_site.admin_view(self.delete_company), name='delete-company'),
        ]
        return custom_urls + urls

    # Activate company
    def activate_company(self, request, pending_company_id):
        activating_user = request.user
        company_info = activate_pending_company(pending_company_id, activating_user)
        self.message_user(request, f'Company "{company_info.company_name}" activated successfully.')
        return redirect('/admin/auth_system/pendingcompany/')

    # Delete company
    def delete_company(self, request, pending_company_id):
        pending_company = get_object_or_404(PendingCompany, pk=pending_company_id)
        name = pending_company.company_name
        pending_company.delete()
        self.message_user(request, f'Pending company "{name}" has been deleted.', level='warning')
        return redirect('/admin/auth_system/pendingcompany/')



# -------------------------
# Location 
# -------------------------
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "division", "district", "upazila", "status", "added_at", "updated_at")
    list_filter = ("status", "division", "district")
    search_fields = ("division", "district", "upazila")
    ordering = ("division", "district")
    readonly_fields = ("added_at", "updated_at")


# -------------------------
# Bank 
# -------------------------
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "name", "email", "phone", "location", "status", "added_at", "updated_at")
    list_filter = ("status", "location__division", "location__district")
    search_fields = ("user_id", "name", "email", "phone", "address")
    ordering = ("name",)
    readonly_fields = ("added_at", "updated_at")


# -------------------------
# Payment Method
# -------------------------
@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "added_at", "updated_at")
 

