from django.contrib import admin
from .models import Parts


class PartsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'price', 'date_pub']
    list_filter = ['date_pub']


admin.site.register(Parts, PartsAdmin)
# Register your models here.
