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

    

def post_detail(request, pk):
    post = get_object_or_404(Company, pk=pk)
    empresa = Company.objects.filter(id=pk).values_list('name','logo','department')
    dadosEmpresa = empresa[0]
    nomeEmpresa = dadosEmpresa[0]
    logoEmpresa = dadosEmpresa[1]
    departamentos =dadosEmpresa[2]
    departamentos = Department.objects.filter(company=post)

    return render(request, 'core/user_form.html', {'post':empresa,'nomeEmpresa':nomeEmpresa,'logoEmpresa':logoEmpresa,'departamentos':departamentos})