from django.urls import path
from voti.views import index, view_a, view_b , view_c, view_d

app_name="voti"

urlpatterns=[
    path('index', index , name="index"),
    path('materie', view_a , name="materie"), 
    path("materieVoti", view_b , name="materieVoti"),
    path("Mediavoti", view_c , name="Mediavoti"),
    path("MaxMin", view_d , name="MaxMin"), 
]