# from django.shortcuts import render
# from django.views.generic import TemplateView
# Create your views here.

# Needed to get yur first page up and running
# class SplashView(TemplateView):
#	template_name = "index.html"

# Used for App 
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class LandingView(TemplateView):
    template_name = 'base/index.html'