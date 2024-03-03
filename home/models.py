from django.db import models

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
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"