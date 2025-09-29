from django.db import models
from apps.auth_system.models import CompanyInfo, Location
from django.contrib.auth.hashers import make_password

# Create your models here.
# -------------------------
# User Role
# -------------------------
class UserRole(models.Model):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


# -------------------------
# User Info Table (Activated Users)
# -------------------------
class UserInfo(models.Model):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
    RELIGION_CHOICES = [
        ('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'), ('Other', 'Other')
    ]

    user_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=15, choices=RELIGION_CHOICES, null=True, blank=True)
    nid = models.CharField(max_length=100, null=True, blank=True)
    passport = models.CharField(max_length=100, null=True, blank=True)
    driving_license = models.CharField(max_length=100, null=True, blank=True)
    corporate_id = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
   
    activated_at = models.DateTimeField(null=True, blank=True)

    @property
    def activated_by_name(self):
        return self.activated_by.username if self.activated_by else "Not activated"

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
# -------------------------
#Branch
# -------------------------
class Branch(models.Model):
    id = models.BigAutoField(primary_key=True)
    store_name = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.SmallIntegerField(default=1, help_text="1 = Active, 0 = Inactive")
    added_at = models.DateTimeField(auto_now_add=True)   # useCurrent()
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "Branch"

    def __str__(self):
        return self.store_name
