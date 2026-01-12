from django.shortcuts import render, get_object_or_404
from .models import Articolo,Giornalista

# def home(request):
#     a=""
#     g=""
#     for art in Articolo.objects.all():
#         a+=(art.titolo+"<br>")
#     response = "Articoli: <br>"+ a + "<br>Giornalisti:<br>"+ g
    
#     return HttpResponse("<h1>"+ response +"</h1>")
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