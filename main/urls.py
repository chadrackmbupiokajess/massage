from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('reservation/<int:service_id>/', views.reservation_view, name='reservation'),
    path('reservation/confirmation/<int:reservation_id>/', views.reservation_confirmation_view, name='reservation_confirmation'),
]
