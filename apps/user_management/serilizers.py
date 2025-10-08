from rest_framework import serializers
from .models import *


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = [ 'role' ]
        
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [ 'id', 'store_name', 'division', 'location', 'address' ]