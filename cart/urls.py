from django.urls import path
from .import views
from .views import cart_add
app_name = 'cart'


urlpatterns = [
    path('cart/', views.cart_add, name='cart')
]