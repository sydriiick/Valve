from django.contrib import admin
from .models import *

admin.site.site_header = "Admin"
admin.site.site_title ="Admin Area"
admin.site.index_title ="Welcome to Admin Area"

class ShutdownValeAdmin(admin.ModelAdmin):
    list_display = ['id','station_four','station_five','station_six','created_on']
    search_fields = ['id','station_four','station_five','station_six','created_on']

admin.site.register(ShutdownValve, ShutdownValeAdmin)