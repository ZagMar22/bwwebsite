from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="Index"),
    path("budowa", views.budowa, name="budowa"),
    path("Index", views.Index, name="Index"),
    path("KalkulatorHP", views.KalkulatorHP, name="KalkulatorHP"),
    path("linki", views.linki, name="linki"),
    path("memy", views.memy, name="memy"),

]