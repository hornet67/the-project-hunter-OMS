from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.auth_system.models import CompanyInfo
# Create your models here.

from django.db import models
from django.core.validators import MinValueValidator
from apps.auth_system.models import CompanyInfo  # adjust import path if needed


# -------------------------
# Main Group
# -------------------------
class MainGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


# -------------------------
# Manufacturer
# -------------------------
class Manufacturer(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    type = models.CharField(max_length=23)
    main_group = models.ForeignKey(MainGroup, on_delete=models.CASCADE, related_name='manufacturers')
    name = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


# -------------------------
# Category
# -------------------------
class Category(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    type = models.CharField(max_length=23)
    main_group = models.ForeignKey(MainGroup, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


# -------------------------
# Forms
# -------------------------
class Forms(models.Model):
    company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
    type = models.CharField(max_length=23)
    main_group = models.ForeignKey(MainGroup, on_delete=models.CASCADE, related_name='forms')
    name = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


# -------------------------
# Units
# -------------------------
class Units(models.Model):
    type = models.CharField(max_length=23)
    main_group = models.ForeignKey(MainGroup, on_delete=models.CASCADE, related_name='units')
    unit_name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.unit_name


# -------------------------
# Product
# -------------------------
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    form = models.ForeignKey(Forms, on_delete=models.CASCADE)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)

    group = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    cp = models.FloatField(validators=[MinValueValidator(0.0)])
    mrp = models.FloatField(validators=[MinValueValidator(0.0)])

    company_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.product_name

    
    
#/////////////////////////////////////////////////////////////////


# class Manufacturer(models.Model):
#     company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=23)
#     status = models.SmallIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True,null= True, blank= True)

#     def __str__(self):
#         # Display company_id and company_name in admin dropdowns
#         return f"{self.company_id} - {self.name}"


# class Category(models.Model):
#     company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=23)
#     status = models.SmallIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True,null= True, blank= True)

#     def __str__(self):
#         return self.name
    
# class Forms(models.Model):
#     company_id = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=23)
#     status = models.SmallIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True,null= True, blank= True)

#     def __str__(self):
#         return self.name
    
# class Units(models.Model):
#     unit_name = models.CharField(max_length=100)
#     company_id = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
#     status = models.SmallIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

#     def __str__(self):
#         return self.unit_name
    
    
# class MainGroup(models.Model):
#     name = models.CharField(max_length=100)
#     manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE, related_name='manufacturers')
#     catagory = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='catagories')
#     forms = models.ForeignKey(Forms,on_delete=models.CASCADE, related_name='forms')
#     unit = models.ForeignKey(Units,on_delete=models.CASCADE, related_name='units')
#     status = models.SmallIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
  
    