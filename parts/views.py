from django.shortcuts import render
from .models import Parts
from django.views.generic import ListView


class Partsview(ListView):
    model = Parts
    fields = ['name', 'description', 'image', 'price']
    template_name = 'part.html'

    def get_context_data(self, **kwargs):
        context = super(Partsview, self).get_context_data(**kwargs)
        context['var1'] = Parts.objects.all()[:3]
        context['var2'] = Parts.objects.all()[3:6]
        context['var3'] = Parts.objects.all()[6:9]
        context['var4'] = Parts.objects.all()[9:]
        return context
# Create your views here.
