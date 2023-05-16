from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ToDoList, Item, Topic, Ksiazka, Zamowienie#, Profile
from .forms import AddTopic, AddDrin, AddKsiazka
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
User = get_user_model()

import matplotlib.pyplot as plt
import numpy as np

# Create your views here.

def budowa(response):
    return render(response, "main/budowa.html", {})


def Index(response):
    return render(response, "main/Index.html", {})

def KalkulatorHP(response):
    return render(response, "main/KalkulatorHP.html", {})

def linki(response):
    return render(response, "main/linki.html", {})

def memy(response):
    return render(response, "main/memy.html", {})




