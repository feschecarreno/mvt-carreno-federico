from django.shortcuts import render

def index(request):
    return render(request, "desafio/familiares.html")
    