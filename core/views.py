from django.shortcuts import render, redirect
from core.models import Evento
# Create your views here.

def lista_eventos(request):
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario) #no lugar de .get(id=1) pode colocar .all() para pegar todos
    evento = Evento.objects.all() #no lugar de .get(id=1) pode colocar .all() para pegar todos
    dados = {"eventos": evento}
    return render(request, "agenda.html", dados)

# def index(request): #para redirecionar a página
#     return redirect("/agenda/")