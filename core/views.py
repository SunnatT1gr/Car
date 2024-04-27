from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

