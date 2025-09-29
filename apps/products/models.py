from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Manufacturer(models.Model):
    company_id = models.CharField(max_length=23, unique=True)
    company_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=23)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True,null= True, blank= True)

    def __str__(self):
        # Display company_id and company_name in admin dropdowns
        return f"{self.company_id} - {self.company_name}"


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    type = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,related_name="type_categories")
    company = models.ForeignKey(Manufacturer,on_delete=models.CASCADE,related_name="company_categories")
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.category_name
    
class Forms(models.Model):
    form_name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.form_name
    
class Units(models.Model):
    unit_name = models.CharField(max_length=100)
    company_id = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.unit_name
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    form = models.ForeignKey(Forms,on_delete=models.CASCADE)
    unit = models.ForeignKey(Units,on_delete=models.CASCADE)
    
    group = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    cp = models.FloatField(validators=[MinValueValidator(0.0)])
    mrp = models.FloatField(validators=[MinValueValidator(0.0)])
    
    company_id = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.product_name

    