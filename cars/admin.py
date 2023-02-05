from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Car)
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Car information", {"fields": ["model", "brand"]}),
        ("Time information", {"fields": ["year"]}),
    ]


admin.site.register(Car, CarAdmin)
