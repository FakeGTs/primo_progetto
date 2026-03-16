from django.shortcuts import get_object_or_404, redirect, render
from forms_app.models import Contatto
from .forms import FormContatto
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

# def contatti(request): view precedente senza gestione del form
#     form = FormContatto()
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
            nuovo_contatto = form.save()

            print("Nuovo contatto creato:", nuovo_contatto)
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

@login_required(login_url="/accounts/login")
def modifica_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)
    if request.method == "POST":
        form = FormContatto(request.POST, instance=contatto)
        if form.is_valid():
            form.save()
            return redirect("forms_app:lista-contatti")
    else:
        form = FormContatto(instance=contatto)
    context = {
        "form": form,
        "contatto": contatto
    }
    return render(request, "modifica_contatto.html", context)

@staff_member_required(login_url="/accounts/login")
def elimina_contatto(request, pk):
    contatto = get_object_or_404(Contatto, id=pk)

    if request.method == "POST":  # vuol dire che l'utente ha inviato il form che conferma l'eliminazione
        contatto.delete()  # elimina il contatto dal database
        return redirect('forms_app:lista-contatti')

    context = {'contatto': contatto}
    return render(request, 'elimina_contatto.html', context)