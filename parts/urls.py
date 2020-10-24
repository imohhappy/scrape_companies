from django.urls import path
from .views import Partsview
from . import views
app_name = 'parts'

urlpatterns = [
    path('', Partsview.as_view(), name='first'),
]