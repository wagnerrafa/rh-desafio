from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Department, Employee

# Create your views here.
def index(request):
    empresas = Company.objects.all()
    
    return render(request, 'core/empresa.html',{'empresas':empresas})

def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'core/cadastrar.html')
    elif (request.method == 'POST'):
        empresa = Company()
        empresa.logo = request.FILES['logo']
        empresa.name = request.POST['nome']
        empresa.legal_number = request.POST['numero']
        empresa.save()
        return redirect('core:index')

def empresa(request, pk):
    post = get_object_or_404(Company, pk=pk)
    empresa = Company.objects.filter(id=pk).values_list('name','logo','department')
    dadosEmpresa = empresa[0]
    nomeEmpresa = dadosEmpresa[0]
    logoEmpresa = dadosEmpresa[1]
    departamentos =dadosEmpresa[2]
    departamentos = Department.objects.filter(company=post)
    
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
       
    return render(request, 'core/user_form.html', {'post':empresa,'nomeEmpresa':nomeEmpresa,'logoEmpresa':logoEmpresa,'departamentos':departamentos})

def colaborador(request):
    if request.method == 'POST':
        colaborador = Employee()
        colaborador.name = request.POST['name']
        colaborador.save()
       
    return render(request, 'core/user_form.html')
