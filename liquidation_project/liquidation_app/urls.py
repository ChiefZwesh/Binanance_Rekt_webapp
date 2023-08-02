from django.urls import path
from .views import dashboard, about, contact

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
