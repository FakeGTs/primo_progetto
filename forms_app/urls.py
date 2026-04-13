from django.urls import path
from forms_app.views import contatti, elimina_contatto , index, lista_contatti, modifica_contatto

app_name="forms_app"

urlpatterns=[
    path('index', index , name="index"),
    path('contattaci', contatti , name="contatti"),
    path('lista_contatti', lista_contatti , name="lista_contatti"),
    path('elimina/<int:pk>/', elimina_contatto, name='elimina_contatto'),
    path('modifica/<int:pk>/', modifica_contatto, name='modifica_contatto'),
]
