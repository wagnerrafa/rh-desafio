from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    empresa = Company.objects.all()
    for i in empresa:
        logo = i.logo
        nomeEmpresa = i.name
    return render(request, 'core/user_form.html',{'logo':logo,'nomeEmpresa':nomeEmpresa})