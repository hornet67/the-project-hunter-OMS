from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import PendingCompany
from .serializers import PendingCompanySerializer


# -------------------------------
# JWT Token Helper
# -------------------------------
def get_tokens_for_company(company):
    refresh = RefreshToken.for_user(company)
    refresh['company_name'] = company.company_name
    refresh['email'] = company.email
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }


# -------------------------------
# Company Register View
# -------------------------------
class CompanyRegisterView(View):
    template_name = 'auth_system/register.html'

    def get(self, request):
        return render(request, self.template_name, {'data': {}, 'messages_list': []})

    def post(self, request):
        data = request.POST
        serializer = PendingCompanySerializer(data=data)
        messages_list = []

        if serializer.is_valid():
            company_name = serializer.validated_data['company_name']

            # Check duplicate
            if PendingCompany.objects.filter(company_name=company_name).exists():
                messages_list.append({'tag': 'warning', 'text': f'⚠️ Company "{company_name}" already exists!'})
                return render(request, self.template_name, {'data': data, 'messages_list': messages_list})

            # Save company
            company = serializer.save()
            messages_list.append({'tag': 'success', 'text': f'✅ Company "{company.company_name}" registered successfully!'})
            
            # Return to same page with success message
            return render(request, self.template_name, {'data': {}, 'messages_list': messages_list})

        else:
            messages_list.append({'tag': 'error', 'text': '❌ Please fill in all required fields correctly.'})
            return render(request, self.template_name, {'data': data, 'messages_list': messages_list})
# -------------------------------
# Company Login View
# -------------------------------
class CompanyLoginView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # render the login form page
        return render(request, 'auth_system/login.html')

    def post(self, request):
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')

        try:
            company = PendingCompany.objects.get(company_name=company_name, email=email)
            token = get_tokens_for_company(company)

            # You can store token in session if needed
            request.session['access_token'] = token['access']
            request.session['refresh_token'] = token['refresh']

            messages.success(request, f'Welcome back, {company.company_name}!')
            return redirect('dashboard')  # or wherever you want
        except PendingCompany.DoesNotExist:
            messages.error(request, 'Invalid company name or email!')
            return redirect('login')


# -------------------------------
# Protected Endpoint (for testing)
# -------------------------------
class CompanyProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        company = request.user
        return render(request, 'auth_system/profile.html', {'company': company})
