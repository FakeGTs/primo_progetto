from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Articolo, Giornalista
import datetime

# 1. Homepage (rinominata in homeview per combaciare con il tuo urls.py)
def homeview(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    return render(request, "news/homepage.html", context)

# 2. Indice
def index(request):
    return render(request, "news/index.html")

# 3. Dettaglio Articolo
def ArticoloDetailView(request, pk):
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

# 4. Lista Articoli
def listaArticoli(request, pk=None):
    if pk is None:
        articoli = Articolo.objects.all()
        giornalista = None
        is_giornalista = False
    else:
        articoli = Articolo.objects.filter(giornalista_id=pk)
        giornalista = get_object_or_404(Giornalista, pk=pk)
        is_giornalista = True
    
    context = {
        'articoli': articoli,
        'is_giornalista': is_giornalista,
        'giornalista': giornalista
    }
    return render(request, 'lista_articoli.html', context)

# 5. Pagina delle Query
def queryBase(request):
    # Query 1-15
    articoli_cognome = Articolo.objects.filter(giornalista__cognome="Antonini")
    numero_totale_articoli = Articolo.objects.count()
    
    # Gestione errore se l'ID 1 non esiste
    try:
        giornalista_1 = Giornalista.objects.get(id=1)
        numero_articoli_giornalista_1 = Articolo.objects.filter(giornalista=giornalista_1).count()
    except Giornalista.DoesNotExist:
        numero_articoli_giornalista_1 = 0
    
    articoli_ordinati = Articolo.objects.order_by('-visualizzazioni')
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)
    articolo_piu_visualizzato = Articolo.objects.order_by('-visualizzazioni').first()
    
    giornalisti_data = Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990, 1, 1))
    articoli_del_giorno = Articolo.objects.filter(data=datetime.date(2023, 1, 1))
    
    giornalisti_periodo = Articolo.objects.filter(data__range=(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31)))
    
    giornalisti_nati = Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980, 1, 1))
    articoli_giornalisti = Articolo.objects.filter(giornalista__in=giornalisti_nati)
    
    giornalista_giovane = Giornalista.objects.order_by('-anno_di_nascita').first()
    giornalista_vecchio = Giornalista.objects.order_by('anno_di_nascita').first()
    
    ultimi = Articolo.objects.order_by('-data')[:5]
    articoli_minime_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)
    articoli_parola = Articolo.objects.filter(titolo__icontains='importante')

    # Query Avanzate 16-20
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()
    articoli_con_and = Articolo.objects.filter(giornalista__anno_di_nascita__gt=datetime.date(1990, 1, 1), visualizzazioni__gte=50)
    articoli_con_or = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=datetime.date(1990, 1, 1)) | Q(visualizzazioni__lte=50))
    articoli_con_not = Articolo.objects.exclude(giornalista__anno_di_nascita__lt=datetime.date(1990, 1, 1))

    context = {
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'giornalisti_periodo': giornalisti_periodo,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_vecchio': giornalista_vecchio,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
        'articoli_mese_anno': articoli_mese_anno,
        'giornalisti_con_articoli_popolari': giornalisti_con_articoli_popolari,
        'articoli_con_and': articoli_con_and,
        'articoli_con_or': articoli_con_or,
        'articoli_con_not': articoli_con_not,
    }

    return render(request, "query.html", context)

def GiornalistaDetailView(request, pk):
    giornalista = get_object_or_404(Giornalista, pk=pk)
    articoli = Articolo.objects.filter(giornalista=giornalista)
    context = {"giornalista": giornalista, "articoli": articoli}
    return render(request, "giornalista_detail.html", context)