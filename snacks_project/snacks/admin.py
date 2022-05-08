from django.contrib import admin
from .models import Snack

# Register your models here.

@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'calories')
