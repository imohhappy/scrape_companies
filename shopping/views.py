from django.shortcuts import render
from .models import Shopping
from django.views.generic import ListView


class Shoppingview(ListView):
    model = Shopping
    fields = ['name', 'description', 'image', 'price']
    template_name = 'shop.html'

    def get_context_data(self, **kwargs):
        context = super(Shoppingview, self).get_context_data(**kwargs)
        context['var'] = Shopping.objects.all()[:3]
        context['var4'] = Shopping.objects.all()[3:]
        return context
# Create your views here.
