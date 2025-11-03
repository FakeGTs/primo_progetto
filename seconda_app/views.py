from django.shortcuts import render
import datetime

def index(request):
    return render(request, "seconda_app/index.html")
def es_if(request):
    context={
        'var1':200,
        'var2':200,
        'var3':300,
    }
    return render(request, "es_if.html", context)
def if_else_elif(request):
    context={
        'var1':100,
        'var2':100.0,
        'var3':100.50,
    }
    return render(request, "if_else_elif.html", context)
def es_for(request):
    context={
        'list1':[1,datetime.date(2019,7,16),'Do Not Give Up!'],
        'list2':[1,datetime.date(2019,7,16),'Do Not Give Up!'],
        'my_dict': {'chiave1': 'Valore 1', 'chiave2': 'Valore 2'},
    }
    return render(request, "es_for.html", context)
# Create your views here.
