from django.contrib import admin
from .models import employee, Timetrack
# Register your models here.

admin.site.register(employee)
admin.site.register(Timetrack)
#admin.site.register(staff)