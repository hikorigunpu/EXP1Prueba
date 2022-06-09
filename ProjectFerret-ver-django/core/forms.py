from django import forms
from django.forms import ModelForm
from .models import obra, user

class obraform(ModelForm):
    class Meta:
        model = obra
        fields = ['idobra','autor','nombre','descripcion','nombretecnica','precio','imagen']

class userform(ModelForm):
    class Meta:
        model = user
        fields = ['username','password']
        