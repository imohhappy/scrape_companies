from django.contrib import admin
from .models import Shopping


class ShoppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image', 'price', 'date_pub']
    list_filter = ['date_pub']


admin.site.register(Shopping, ShoppingAdmin)
# Register your models here.
