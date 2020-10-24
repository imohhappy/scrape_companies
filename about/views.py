from django.shortcuts import render
from .models import About
from django.views.generic import ListView


class Aboutview(ListView):
    model = About
    fields = ['name', 'description', 'image', 'price']
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(Aboutview, self).get_context_data(**kwargs)
        context['vat'] = About.objects.all()[:1]
        context['vat4'] = About.objects.all()[1:2]
        context['vat5'] = About.objects.all()[2:3]
        context['vat6'] = About.objects.all()[3:4]

        return context
# Create your views here.
