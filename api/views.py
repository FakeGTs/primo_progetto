from django.shortcuts import render
import requests

def index(request):
    return render(request, 'api/index.html')

def todos_view(request):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/todos/')
        

        if response and response.status_code == 200:
            lista_todos = response.json()
            messaggio_errore = None
        else:
            lista_todos = []
            
            messaggio_errore = "Errore nel recupero dei dati.  codice di stato: {}".format(response.status_code)
    except Exception as e:
        lista_todos = []
        messaggio_errore = "Errore nela connessione API: {}".format(str(e))
        
    return render(request, 'api/todos.html', {
        'todos': lista_todos, 
        'messaggio_errore': messaggio_errore
        })


