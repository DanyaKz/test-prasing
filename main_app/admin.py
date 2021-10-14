from django.contrib import admin
from . import models

# Register your models here.

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('resource_name',)
    search_fields = ('resource_name', )

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','res_id','not_date')
    search_fields = ('title',)

admin.site.register(models.Resource, ResourceAdmin)
admin.site.register(models.Item, ItemAdmin)