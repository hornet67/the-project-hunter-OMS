from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# -------------------------
# Custom User Model
# -------------------------
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(
        null=True, blank=True, validators=[MinValueValidator(18), MaxValueValidator(70)]
    )
    phone_number = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username


# -------------------------
# Company Type
# -------------------------
class CompanyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -------------------------
# Pending Company Info
# -------------------------
class PendingCompany(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=11, blank=True)
    type = models.ForeignKey(CompanyType, on_delete=models.CASCADE)
    address = models.TextField()
    website = models.URLField(max_length=200, blank=True)
    domain = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.company_name


# -------------------------
# Company Info (Activated)
# -------------------------
class CompanyInfo(models.Model):
    company_id = models.AutoField(primary_key=True, unique=True)
    company_name = models.CharField(max_length=300)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=11, blank=True)
    type = models.ForeignKey(CompanyType, on_delete=models.CASCADE)
    address = models.TextField()
    website = models.URLField(max_length=200, blank=True)
    domain = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    activated_by = models.ForeignKey(
        'auth_system.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='activated_companies'
    )
    activated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.company_name


# -------------------------
# Activate Pending Company Function
# -------------------------
def activate_pending_company(pending_company_id, activated_by_user):
    pending = PendingCompany.objects.get(company_id=pending_company_id)
    company_info = CompanyInfo.objects.create(
        company_name=pending.company_name,
        email=pending.email,
        phone_number=pending.phone_number,
        type=pending.type,
        address=pending.address,
        website=pending.website,
        domain=pending.domain,
        is_active=True,
        activated_by=activated_by_user,
        activated_at=timezone.now()
    )
    pending.delete()
    return company_info




# -------------------------
# location table
# -------------------------
class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    upazila = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=1)  
    added_at = models.DateTimeField(auto_now_add=True)  #
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  # nullable timestamp

    class Meta:
        db_table = "locations"  

    def __str__(self):
        return f"{self.division} - {self.district} - {self.upazila}"
    
# -------------------------
# bank table
# -------------------------    

class Bank(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1)  
    added_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "banks"

    def __str__(self):
        return self.name if self.name else f"Bank {self.id}"

# -------------------------
# bank table
# ------------------------- 
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)  # 1 = Active, 0 = Inactive
    added_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)  # nullable timestamp
    
    def __str__(self):
        return self.name
