from django.urls import path
from news.views import homeview, ArticoloDetailView, index

app_name="news"

urlpatterns=[
    path('index', index , name="index"),
    path('homeview', homeview , name="homeview"),
    path("articoli/<int:pk>", ArticoloDetailView , name="articolo_detail"),

]