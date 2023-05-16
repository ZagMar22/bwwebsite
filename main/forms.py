from django import forms
from django.forms import ModelForm
from .models import Topic, Ksiazka, Zamowienie


class AddTopic(ModelForm):

    class Meta:
        model = Topic
        fields = ('title', 'search_string', 'asset_description',)


class AddDrin(ModelForm):

    class Meta:
        model = Zamowienie
        fields = ('Drin', 'Uwagi_do_Zamowienia',)
        labels = {
            # 'imie': '',
            # 'nazwisko': '',
            # 'telefon':'',
        }
        widgets = {
            'Drin': forms.TextInput(attrs={'class':'form-control'}),
            'Uwagi_do_Zamowienia': forms.TextInput(attrs={'class':'form-control'}),
        }

class AddKsiazka(ModelForm):

    class Meta:
        model = Ksiazka
        fields = ('imie', 'nazwisko',)
        labels = {
            # 'imie': '',
            # 'nazwisko': '',
            # 'telefon':'',
        }
        widgets = {
            'imie': forms.TextInput(attrs={'class':'form-control'}),
            'nazwisko': forms.TextInput(attrs={'class':'form-control'}),
        }