from django.urls import path
from .views import index, spotify_login, spotify_success, test_spotify, todos_view,spotify_callback

app_name = 'api' # Add this line!

urlpatterns = [
    path('', index, name='index'),
    path('todos/', todos_view, name='todos'),
    path('spotify/', spotify_login, name='spotify_login'),
    path('spotify-callback/', spotify_callback, name='spotify_callback'),
    path('spotify-success/',spotify_success, name='spotify_success'),
    path('test-spotify/', test_spotify, name='test_spotify'),
]