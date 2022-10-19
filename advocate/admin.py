from django.contrib import admin

# Register your models here.

from .models import Advocate,Company,Links,Companies

admin.site.register([Advocate,Company,Links,Companies])
