from django.shortcuts import render
from . import models
def home(request):
    return render(request=request, template_name="usuarios/home.html")

def usuarios(request):
    novo_usuario = models.Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    
    usuarios = {
        'usuarios': models.Usuario.objects.all(),
    }
    
    return render(request=request, template_name="usuarios/listagem_usuarios.html", context=usuarios)
    
