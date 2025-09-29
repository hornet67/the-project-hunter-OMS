from django.shortcuts import render

# Create your views here.


def companyregister(request):
    return render(request, 'auth_system/register.html')

def companylogin(request):
    return render(request, 'auth_system/login.html')