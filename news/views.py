from django.shortcuts import HttpResponse
from .models import Artticolo,Giornalista

def home(request):
    return HttpResponse("<h1>Homepage news!</h1>")