from django.urls import path
from prova_pratica_0.views import index,somma,media

app_name="prova_pratica_0"

urlpatterns=[
    path('', index , name="index"),
    path('somma', somma , name="somma"),   
    path('media', media , name="media"),      
    
]