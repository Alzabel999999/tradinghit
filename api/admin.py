from django.contrib import admin
from .models import BurseData
# Register your models here.

@admin.register(BurseData)
class BurseDataAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ('name', )
    readonly_fields = []
    exclude = ['api_key', 'api_secret']
