from django.shortcuts import render

def index(request):
    return render(request,"core/index.html")

def album(request):
    return render(request,"core/album.html")

def info(request):
    return render(request,"core/info.html")

def preguntas(request):
    return render(request,"core/preguntas.html")