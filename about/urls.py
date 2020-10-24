from django.urls import path
from .views import Aboutview

app_name= 'about'
urlpatterns = [
    path('', Aboutview.as_view(), name='about')
]