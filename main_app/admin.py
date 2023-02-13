from django.contrib import admin
from .models import Regimen, Exercise, Doing
# Register your models here.

admin.site.register(Regimen)

admin.site.register(Exercise)

admin.site.register(Doing)