from urllib import request
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from .models import *
from .serilizers import *
from rest_framework.permissions import AllowAny
# -------------------------------
# User Role View
# -------------------------------   

class UserRoleView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        """Display all roles"""
        datas = UserRole.objects.all()
        return render(request, 'user_management/userrole.html', {'datas': datas})

    def post(self, request):
        """Handle Create, Update, Delete actions"""
        action = request.POST.get('action')
        role_id = request.POST.get('id')

        # -------------------------
        # CREATE
        # -------------------------
        if action == "create":
            serializer = UserRoleSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, "✅ User Role created successfully!")
            else:
                messages.error(request, "❌ Failed to create User Role.")
        
        # -------------------------
        # UPDATE
        # -------------------------
        elif action == "update":
            try:
                role = UserRole.objects.get(pk=role_id)
                serializer = UserRoleSerializer(role, data=request.POST, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    messages.success(request, "✏️ User Role updated successfully!")
                else:
                    messages.error(request, "❌ Failed to update User Role.")
            except UserRole.DoesNotExist:
                messages.error(request, "⚠️ Role not found!")

        # -------------------------
        # DELETE
        # -------------------------
        elif action == "delete":
            try:
                role = UserRole.objects.get(pk=role_id)
                role.delete()
                messages.success(request, "🗑️ User Role deleted successfully!")
            except UserRole.DoesNotExist:
                messages.error(request, "⚠️ Role not found!")

        # Always reload page with updated data
        datas = UserRole.objects.all()
        return render(request, 'user_management/userrole.html', {'datas': datas})
# -------------------------------
# Company userinfo View
# -------------------------------   
class UserInfoView(APIView):
    pass


# -------------------------------
# Company premisson View
# -------------------------------   
class UserPermissionsView(APIView):
    pass

# -------------------------------
# Company branch View
# -------------------------------   
class BranchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        datas = Branch.objects.all()
        return render(request, 'user_management/branch.html', {'datas': datas, 'form_data': {}})

    def post(self, request):
        action = request.POST.get('action')
        branch_id = request.POST.get('id')

        # Save POST data in case of error
        form_data = request.POST.dict()

        # CREATE
        if action == "create":
            serializer = BranchSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                messages.success(request, "✅ Branch created successfully!")
                form_data = {}  # clear after success
            else:
                messages.error(request, "❌ Failed to create Branch.")

        # UPDATE
        elif action == "update":
            try:
                branch = Branch.objects.get(pk=branch_id)
                serializer = BranchSerializer(branch, data=request.POST, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    messages.success(request, "✏️ Branch updated successfully!")
                    form_data = {}  # clear after success
                else:
                    messages.error(request, "❌ Failed to update Branch.")
            except Branch.DoesNotExist:
                messages.error(request, "⚠️ Branch not found!")

        # DELETE
        elif action == "delete":
            try:
                branch = Branch.objects.get(pk=branch_id)
                branch.delete()
                messages.success(request, "🗑️ Branch deleted successfully!")
                form_data = {}  # clear after success
            except Branch.DoesNotExist:
                messages.error(request, "⚠️ Branch not found!")

        datas = Branch.objects.all()
        return render(request, 'user_management/branch.html', {'datas': datas, 'form_data': form_data})
