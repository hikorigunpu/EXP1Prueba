from django.contrib import admin
from .models import obra, tecnica, user
# Register your models here.

admin.site.register(tecnica)
admin.site.register(obra)
admin.site.register(user)