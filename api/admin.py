from django.contrib import admin
from .models import *

admin.site.site_header = "Admin"
admin.site.site_title ="Admin Area"
admin.site.index_title ="Welcome to Admin Area"

class StationOneAdmin(admin.ModelAdmin):
    list_display = ['unique','data_1','data_2','data_3']

admin.site.register(StationOne, StationOneAdmin)
admin.site.register(StationTwo)
admin.site.register(Default)