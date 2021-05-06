from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_fields=['name']

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_fields=['size__name','type','toppings']