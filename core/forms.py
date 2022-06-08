from django import forms
from django.forms import ModelForm
from .models import obra

class obraform(ModelForm):
    class Meta:
        model = obra
        fields = ['idobra','autor','nombre','descripcion','nombretecnica','precio','imagen']
        