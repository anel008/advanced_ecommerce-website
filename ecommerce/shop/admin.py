from django.contrib import admin

# Register your models here.
from .models import *


class CatagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(Categ, CatagAdmin)


class ProdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
    list_display = ['name','slug','price','stock','img']
    list_editable=['price','stock','img']
admin.site.register(Products,ProdAdmin)