from django.urls import path
from .views import  form_del_obra, form_mod_obra,form_obra, listadouser,home, login, loginnewuser, index2, obrasform, profile, galery1, galery2, galery3, aboutus, form, formalt, galery1alt, galery2alt, galery3alt, aboutusalt

urlpatterns = [
    path('', home, name="home"),
    path('login', login, name="login"),
    path('index2', index2, name="index2"),
    path('loginnewuser', loginnewuser, name="loginnewuser"),
    path('galery1', galery1, name="galery1"),
    path('galery2', galery2, name="galery2"),
    path('galery3', galery3, name="galery3"),
    path('form', form, name="form"),
    path('aboutus', aboutus, name="aboutus"),
    path('obrasform', obrasform, name="obrasform"),
    path('profile', profile, name="profile"),

    path('aboutusalt', aboutusalt, name="aboutusalt"),
    path('formalt', formalt, name="formalt"),
    path('galery1alt', galery1alt, name="galery1alt"),
    path('galery2alt', galery2alt, name="galery2alt"),
    path('galery3alt', galery3alt, name="galery3alt"),

    path('form_obra', form_obra, name="form_obra"),
    path('form_mod_obra/<id>', form_mod_obra, name="form_mod_obra"),
    path('form-del-obra/<id>', form_del_obra, name="form_del_obra"),
    path('listadouser', listadouser, name="listadouser"),

        
]