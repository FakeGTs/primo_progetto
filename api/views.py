from django.shortcuts import redirect, render
from django.conf import settings
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import json
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



# Funzione helper per ottenere l'oggetto SpotifyOAuth, utile per centralizzare la configurazione
def get_spotify_oauth():
    return SpotifyOAuth(
        client_id=settings.SPOTIPY_CLIENT_ID,
        client_secret=settings.SPOTIPY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIPY_REDIRECT_URI,
        scope=settings.SPOTIPY_SCOPE,
        cache_handler=spotipy.cache_handler.DjangoSessionCacheHandler()
    )

# 1. View per iniziare il login Spotify
def spotify_login(request):
    sp_oauth = get_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

# 2. View per gestire il callback di Spotify
def spotify_callback(request):
    sp_oauth = get_spotify_oauth()
    code = request.GET.get('code')

    if code:
        # Scambia il codice per un token di accesso e un token di refresh
        token_info = sp_oauth.get_access_token(code, check_cache=False)

        # Salva le informazioni del token nella sessione dell'utente
        # In un'applicazione reale, potresti voler salvare questi token in un database
        # associati all'utente Django corrente.
        request.session['token_info'] = token_info
        request.session.modified = True

        return redirect('spotify_success') # Reindirizza a una pagina di successo nella tua app
    else:
        # Gestisci il caso in cui non viene ricevuto un codice (es. utente nega l'autorizzazione)
        return render(request, 'spotify_error.html', {'message': 'Autorizzazione negata o errore.'})

# Esempio di view di successo
def spotify_success(request):
    return render(request, 'spotify_success.html', {'message': 'Autenticazione Spotify riuscita!'})

def test_spotify(request):
    token_info = request.session.get('token_info', None)

    if not token_info:
        # Se non ci sono token, reindirizza l'utente alla pagina di login Spotify
        return redirect('spotify_login')

    # Inizializza SpotifyOAuth con i token esistenti
    sp_oauth = get_spotify_oauth()

    # Controlla se il token di accesso è scaduto e rinfrescalo se necessario
    if sp_oauth.is_token_expired(token_info):
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
        request.session['token_info'] = token_info
        request.session.modified = True

    # Inizializza il client Spotipy con i token attuali
    sp = spotipy.Spotify(auth=token_info['access_token'])

    try:
        results = sp.current_user_saved_tracks()
        lista_canzoni = []
        img_urls = []
        for item in results['items']:
            track_name = item['track']['name']
            artist_name = item['track']['artists'][0]['name']
            img_urls.append(item['track']['album']['images'][0]['url'])
            lista_canzoni.append(f"{track_name} - {artist_name}")

        context = {
            "results": lista_canzoni,
            "img": img_urls,
        }
        return render(request, 'spotify.html', context)
    except Exception as e:
        # Gestisci errori API (es. token non valido anche dopo refresh)
        print(f"Errore durante la chiamata API di Spotify: {e}")
        # Potresti voler cancellare i token e far rifare l'autenticazione all'utente
        if 'token_info' in request.session:
            del request.session['token_info']
        return redirect('spotify_login') # Reindirizza per un nuovo login