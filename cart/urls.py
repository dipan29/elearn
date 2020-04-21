from django.urls import path, register_converter

from . import views

class NegativeIntConverter:
    regex = '-?\d+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value
    
# Registering a Signed Integer
register_converter(NegativeIntConverter, 'sint')

app_name = 'cart'

urlpatterns = [
    path('<sint:last_discount>/<int:courses_added>', views.cart_detail, name='cart_detail'),
    path('', views.cart_detail, name='cart_detail'),
    path('add/bundle/<slug:slug>/', views.cart_add_bundle, name='cart_add_bundle'),
    path('add/<slug:slug>/', views.cart_add, name='cart_add'),
    path('remove/<slug:slug>', views.cart_remove, name='cart_remove'),
    path('checkout/<int:amount>', views.cart_checkout, name='cart_checkout'),
]
