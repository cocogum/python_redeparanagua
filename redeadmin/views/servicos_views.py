from django.shortcuts import redirect, render
from ..forms.servicos_forms import ServicosForm
from ..models import Servicos
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def cadastrar_servicos(request):
    if request.method == "POST":
        form_servicos = ServicosForm(request.POST)
        if form_servicos.is_valid():
            form_servicos.save()
            return redirect('listar_servicos')
    else: 
        form_servicos = ServicosForm()
    return render(request, 'servicos/form_servicos.html', {"form_servicos": form_servicos})

@login_required
def listar_servicos(request):
    servicos = Servicos.objects.all()
    return render(request, 'servicos/lista_servicos.html', {"servicos": servicos})

@login_required
def editar_servicos(request, id):
    servicos = Servicos.objects.get(id=id)
    form_servicos = ServicosForm(request.POST or None, instance=servicos)
    if form_servicos.is_valid():
        form_servicos.save()
        return redirect('listar_servicos')
    return render(request, 'servicos/form_servicos.html', {'form_servicos': form_servicos})



