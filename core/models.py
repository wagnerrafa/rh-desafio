import uuid
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from cloudinary.models import CloudinaryField


# Create your models here.

class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    logo = CloudinaryField('Foto de logo')
    name = models.CharField(max_length=50, verbose_name='Nome', blank=False)
    legal_number = models.CharField(max_length=10, verbose_name='Numero', blank=False)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    def __str__(self):
        return(self.name)
    def get_absolute_url(self):
        return reverse('core:edit_company', kwargs={'pk': self.pk})

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    company = models.ForeignKey(Company, verbose_name="Empresa", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Nome', blank=False)
    status = models.BooleanField('status', default=False)
    admin = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)
    def __str__(self):
        return(self.name )
    def get_absolute_url(self):
        return reverse('core:edit_department', kwargs={'pk': self.pk})
    
class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    department = models.ForeignKey(Department, verbose_name="Departamento", on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')

    )
    email = models.EmailField(verbose_name='Email', max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER)
    # department = models.ForeignKey(Department, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, default='Sem Telefone')
    user = models.CharField(max_length=50, verbose_name='Nome do usuario')
    age = models.IntegerField(default=0)
    joining_date = models.DateField(null=True)
    salary = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    # This is auto created and updated date
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    create_user = models.UUIDField(editable=False, null=True)
    update_user = models.UUIDField(editable=False, null=True)

    # Simple title return queue for django admin or auto template
    def __str__(self):
        return str(self.name)
        
    def get_absolute_url(self):
        return reverse('core:edit_employee', kwargs={'pk': self.pk})
