from django.shortcuts import render
from desafio.models import Familiar

def index(request):
    return render(request, "desafio/familiares.html")

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "desafio/familiares.html", {"lista_familiares": lista_familiares})

