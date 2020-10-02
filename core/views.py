from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Department, Employee
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    empresas = Company.objects.all()
    
    return render(request, 'core/empresa.html',{'empresas':empresas})

def empresa(request, pk):
    post = get_object_or_404(Company, pk=pk)
    empresa = Company.objects.filter(id=pk).values_list('name','logo','department')
    dadosEmpresa = empresa[0]
    nomeEmpresa = dadosEmpresa[0]
    logoEmpresa = dadosEmpresa[1]
    departamentos =dadosEmpresa[2]
    departamentos = Department.objects.filter(company=post)
    msg = ''
    if request.method == 'POST':
        colaborador = Employee()
        colaborador.name = request.POST['name']
        colaborador.phone = request.POST['telefone']
        colaborador.age = request.POST['idade']
        colaborador.salary = request.POST['salario']
        colaborador.gender = request.POST['genero']
        colaborador.joining_date = request.POST['entrada']
        colaborador.user = request.POST['user']
        colaborador.company_id = pk
        colaborador.email = request.POST['email']
        colaborador.department_id = request.POST['departamento']

        colaborador.save()
        msg = "Cadastro feito com sucesso"
    return render(request, 'core/user_form.html', {'post':empresa,'nomeEmpresa':nomeEmpresa,'logoEmpresa':logoEmpresa,'departamentos':departamentos,'msg':msg})


class EmployeeList(ListView):
    model = Employee

class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'email','phone','user','age','joining_date','salary','gender','company','department']
    success_url = reverse_lazy('core:employee_list')

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'email','phone','user','age','joining_date','salary','gender','company','department']
    success_url = reverse_lazy('core:employee_list')

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('core:employee_list')

class DepartmentList(ListView):
    model = Department

class DepartmentCreate(CreateView):
    model = Department
    fields = ['company','name','status']
    success_url = reverse_lazy('core:department_list')

class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['company','name','status']
    success_url = reverse_lazy('core:department_list')

class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('core:department_list')

class CompanyList(ListView):
    model = Company

class CompanyCreate(CreateView):
    model = Company
    fields = ['logo','name','legal_number']
    success_url = reverse_lazy('core:company_list')

class CompanyUpdate(UpdateView):
    model = Company
    fields = ['logo','name','legal_number']
    success_url = reverse_lazy('core:company_list')

class CompanyDelete(DeleteView):
    model = Company
    success_url = reverse_lazy('core:company_list')