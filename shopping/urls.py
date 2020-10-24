from django.urls import path
from  .views import Shoppingview

app_name= 'shop'
urlpatterns = [
    path('', Shoppingview.as_view(), name='shop')
]