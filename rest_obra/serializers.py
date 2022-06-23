from django.db.models import fields
from rest_framework import serializers
from core.models import obra

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = obra
        fields = ['idobra','autor','nombre','descripcion','nombretecnica','precio','imagen'] 