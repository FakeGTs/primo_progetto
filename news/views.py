from django.shortcuts import render, get_object_or_404
from .models import Articolo,Giornalista

def index(request):
    return render(request, "news/index.html")
def homeview(request):
    articoli =Articolo.objects.all()
    giornalisti =Giornalista.objects.all()
    context={"articoli" : articoli, "giornalisti" : giornalisti}
    print(context)
    return render(request, "homeview.html", context)
def ArticoloDetailView(request, pk):
    articolo=get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render (request,"articolo_detail.html", context)

def listaArticoli(request,pk=None):
    if(pk==None):
        articoli=Articolo.objects.all()
        giornalista=None
    else:
        articoli=Articolo.objects.filter(giornalista_id=pk)
        giornalista=Giornalista.objects.get(pk=pk)
    if(pk==None):
        is_giornalista=False
    else:
        is_giornalista=True
    context={
        'articoli':articoli,
        'is_giornalista':is_giornalista,
        'giornalista':giornalista
    }

    return render(request, 'lista_articoli.html',context)