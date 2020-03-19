from django.urls import path
from .views import *
from django.views.generic import TemplateView


app_name = 'root'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
    
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('privacy/', TemplateView.as_view(template_name="privacy.html"), name='privacy'),
    path('tnc/', TemplateView.as_view(template_name="tnc.html"), name='tnc'),
    path('services/', TemplateView.as_view(template_name="services.html"), name='services'),
    path('faqs/', TemplateView.as_view(template_name="faqs.html"), name='faqs'),
]
