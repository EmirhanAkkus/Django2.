from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class AnasayfaView(TemplateView):
    template_name = 'home.html'

class BlogView(TemplateView):
    template_name= 'blog.html'