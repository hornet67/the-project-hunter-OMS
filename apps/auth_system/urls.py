from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import *


urlpatterns = [
    path('', CompanyRegisterView.as_view(), name='register'),
    path('login/', CompanyLoginView.as_view(), name='login'),
    path('logout/', CompanyLogoutView.as_view(), name='logout'),
    path('dashboard/', CompanyDashboardView.as_view(), name='dashboard'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
