from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, "prova_pratica_0/index.html")

def media(request):
    num=[]
    sommaM=0
    for i in range(30):
        n = random.randint(1,10)
        num.append(n)
        sommaM=sommaM+n 
    media=sommaM/len(num)
    context={
        'Lista': num,
        'media': round(media,2),
    }
    return render(request, "prova_pratica_0/media.html", context)

def somma(request):
    n1= random.randint(1,10)
    n2= random.randint(1,10)
    somma=n1+n2
    context={
        'n1': n1,
        'n2': n2,
        'somma': somma,
    }
    return render(request, "prova_pratica_0/somma.html", context)
