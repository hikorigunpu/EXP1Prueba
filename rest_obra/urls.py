from django.urls import path
from rest_obra.views import lista_obras, detalle_obra
from rest_obra.viewsLogin import loginauth

urlpatterns = [
    path('lista_obras', lista_obras, name='lista_obras'),
    path('detalle_obra/<id>', detalle_obra, name= 'detalle_obra'),
    path('loginauth', loginauth, name = 'loginauth')
]