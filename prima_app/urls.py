from django.urls import path
from prima_app.views import homepage,welcome,lista,chiSiamo

app_name="prima_app"

urlpatterns=[
    path('', homepage, name="homepage"),
    path('welcome', welcome, name="welcome"),
    path('lista', lista, name="lista"),
    path('chi_siamo', chiSiamo, name="chi_siamo"),
]