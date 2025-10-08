from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import PendingCompany
from .serializers import PendingCompanySerializer


# -------------------------------
# JWT Token Helper
# -------------------------------
def get_tokens_for_company(company):
 
    refresh = RefreshToken()
    refresh['company_name'] = company.company_name
    refresh['email'] = company.email

    access = refresh.access_token

    return {
        'refresh': str(refresh),
        'access': str(access)
    }
# -------------------------------
# Company Register View
# -------------------------------

class CompanyRegisterView(APIView):
    permission_classes = [AllowAny]
    template_name = 'auth_system/register.html'

    def get(self, request):
        # Render the registration page with empty form
        return render(request, self.template_name, {'data': {}, 'messages_list': []})

    def post(self, request):
        serializer = PendingCompanySerializer(data=request.data)
        messages_list = []

        if serializer.is_valid():
            company_name = serializer.validated_data['company_name']

            # Check duplicate
            if PendingCompany.objects.filter(company_name=company_name).exists():
                messages_list.append({
                    'tag': 'warning',
                    'text': f'⚠️ Company "{company_name}" already exists!'
                })
                return render(request, self.template_name, {'data': request.data, 'messages_list': messages_list})

            # Save company
            company = serializer.save()
            messages_list.append({
                'tag': 'success',
                'text': f'✅ Company "{company.company_name}" registered successfully!'
            })
            return render(request, self.template_name, {'data': {}, 'messages_list': messages_list})

        # Invalid serializer
        messages_list.append({
            'tag': 'error',
            'text': '❌ Please fill in all required fields correctly.'
        })
        return render(request, self.template_name, {'data': request.data, 'messages_list': messages_list})

# -------------------------------
# Company Login View
# -------------------------------
class CompanyLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'auth_system/login.html')

    def post(self, request):
        company_name = request.data.get('company_name')
        email = request.data.get('email')

        try:
            company = PendingCompany.objects.get(company_name=company_name, email=email)

            # Store company info in session (acts as "login")
            request.session['company_id'] = company.id
            request.session['company_name'] = company.company_name

            messages.success(request, f'Welcome  {company.company_name}!')
            return redirect('dashboard')
        except PendingCompany.DoesNotExist:
            messages.error(request, 'Invalid company name or email!')
            return redirect('login')
        
# -------------------------------
# Company Logout View
# -------------------------------       
class CompanyLogoutView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Clear all session data
        request.session.flush()
        
        
        # Redirect to login page
        return redirect('login')


# -------------------------------
# Protected Endpoint (for testing)
# -------------------------------
class CompanyDashboardView(APIView):
    permission_classes = [AllowAny]  # no JWT required
    template_name = 'auth_system/dashboard.html'

    def get(self, request):
        company_id = request.session.get('company_id')
        if not company_id:
            messages.error(request, 'Please login first!')
            return redirect('login')

        company = PendingCompany.objects.get(id=company_id)
        return render(request, self.template_name, {'company': company})
