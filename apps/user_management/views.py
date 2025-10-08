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

    # Render HTML dashboard
    def get(self, request):
        datas = UserRole.objects.all()
        return render(request, 'user_management/userrole.html', {'datas': datas})

    # Add new role
    def post(self, request):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            role = serializer.save()
            return Response({"success": True, "id": role.id, "role": role.role}, status=status.HTTP_201_CREATED)
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Update existing role
    def put(self, request, pk):
        try:
            role = UserRole.objects.get(pk=pk)
        except UserRole.DoesNotExist:
            return Response({"success": False, "message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserRoleSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "id": role.id, "role": role.role})
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Delete role
    def delete(self, request, pk):
        try:
            role = UserRole.objects.get(pk=pk)
        except UserRole.DoesNotExist:
            return Response({"success": False, "message": "Role not found"}, status=status.HTTP_404_NOT_FOUND)
        
        role.delete()
        return Response({"success": True})
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
    pass