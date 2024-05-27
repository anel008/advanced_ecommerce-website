from django.contrib import admin

# Register your models here.
from .models import *


class CatagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Categ, CatagAdmin)


class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Products,ProdAdmin)