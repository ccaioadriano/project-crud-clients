from django.shortcuts import render

def home(request):
    return render(request=request, template_name="usuarios/home.html")

def usuarios(request):
    return render(request=request, template_name="usuarios/listagem_usuarios.html")
    
