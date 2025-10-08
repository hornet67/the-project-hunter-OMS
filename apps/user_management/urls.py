from django.urls import path
from .views import *

urlpatterns = [
     path('userrole/', UserRoleView.as_view(), name='userrole'),          # GET & POST
    path('userrole/<int:pk>/', UserRoleView.as_view(), name='userrole'),
    path('userinfo/', UserInfoView.as_view(), name='userinfo'),
    path('userpermissions/', UserPermissionsView.as_view(), name='userpermissions'),
    path('branch/', BranchView.as_view(), name='branch'),
]