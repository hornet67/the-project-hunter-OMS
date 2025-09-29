from django.contrib import admin
from .models import *
# Register your models here.

# -------------------------
# User Role
# -------------------------
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role')
    search_fields = ('role',)


# -------------------------
# Users
# -------------------------
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email', 'phone_number', 'gender', 'role', 'company')
    search_fields = ('name', 'email', 'phone_number', 'nid', 'passport')
    list_filter = ('gender', 'role', 'company', 'religion')
    readonly_fields = ('password',)


# -------------------------
# Branch
# -------------------------       
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("id", "store_name", "division", "location", "status", "added_at", "updated_at")
    list_filter = ("status", "division")
    search_fields = ("store_name", "division", "address")
    list_select_related = ("location",)
    
