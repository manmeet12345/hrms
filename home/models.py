from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length = 15)
    address = models.TextField()
    birth_date = models.DateField(null = True)
    department = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    added_datetime = models.DateTimeField(auto_now_add = True)
    emp_code = models.CharField(max_length=50,null=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
class Timetrack(models.Model):
    employee = models.CharField(max_length=100)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description