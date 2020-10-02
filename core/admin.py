from django.contrib import admin

# Register your models here.
from core.models import Company, Employee, Department, Book

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Company)
admin.site.register(Book)