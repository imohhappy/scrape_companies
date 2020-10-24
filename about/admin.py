from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'price', 'date_pub']
    list_filter = ['date_pub']


admin.site.register(About, AboutAdmin)
# Register your models here.
