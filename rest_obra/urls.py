from django.urls import path
from rest_obra.views import lista_obras, detalle_obra
from rest_obra.viewsLogin import login

urlpatterns = [
    path('lista_obras', lista_obras, name='lista_obras'),
    path('detalle_obra/<id>', detalle_obra, name= 'detalle_obra'),
    path('login', login, name = 'login')
]