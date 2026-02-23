from django.urls import path
from forms_app.views import contatti , index, lista_contatti

app_name="forms_app"

urlpatterns=[
    path('', index , name="index"),
    path('contattaci', contatti , name="contatti"),
    path('lista_contatti', lista_contatti , name="lista_contatti"),

]