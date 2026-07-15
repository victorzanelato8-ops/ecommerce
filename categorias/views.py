from django.shortcuts import render
from .models import Categoria

def home(request):
    categorias = Categoria.objects.all()
    return render(request,'categoria/index.html',{'categorias': categorias})
    

