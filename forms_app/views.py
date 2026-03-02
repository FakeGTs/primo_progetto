from django.shortcuts import render

from forms_app.models import Contatto
from .forms import FormContatto
from django.http import HttpResponse

# def contatti(request): view precedente senza gestione del form
#     form=FormContatto()
#     context = {"form": form}
#     return render(request, "contatto.html", context)

def index(request):
    return render(request, "forms_app/index.html")

def contatti(request):
    if request.method == "POST":
        form = FormContatto(request.POST)
        if form.is_valid():
            print("Form valido!")
            print("Nome:", form.cleaned_data['nome'])
            print("Cognome:", form.cleaned_data['cognome'])
            print("Email:", form.cleaned_data['email'])
            print("Contenuto:", form.cleaned_data['contenuto'])

            print("Dati salvati nel database!")
            nuovo_contatto= form.save()
            print("nuovo post creato:", nuovo_contatto)
            print(nuovo_contatto.nome)
            print(nuovo_contatto.cognome)
            print(nuovo_contatto.email)
            print(nuovo_contatto.contenuto)
            return HttpResponse("<h1>Grazie per averci contattato!</h1>")
    else:
        form = FormContatto()
    
    context = {"form": form}
    return render(request, "contatto.html", context)

def lista_contatti(request):
    contatti = Contatto.objects.all()
    context = {"contatti": contatti}
    return render(request, "lista_contatti.html", context)