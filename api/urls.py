from django.urls import path
from .views import index, todos_view

app_name = 'api' # Add this line!

urlpatterns = [
    path('', index, name='index'),
    path('todos/', todos_view, name='todos'),
]