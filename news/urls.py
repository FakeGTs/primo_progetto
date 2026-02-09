from django.urls import path
from news.views import homeview, ArticoloDetailView, index, listaArticoli, queryBase

app_name="news"

urlpatterns=[
    path('index', index , name="index"),
    path('homeview', homeview , name="homeview"), 
    path("articolo/<int:pk>", ArticoloDetailView , name="articolo_detail"),
    path("lista_articoli", listaArticoli , name="lista_articoli"),
    path("lista_articoli/<int:pk>", listaArticoli , name="lista_articoli"),
    path("query", queryBase , name="query")


]