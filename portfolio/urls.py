
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home , name='home'),
   path('sobre_Fabian/', views.sobre , name='sobre'),
   path('Oferta/', views.oferta , name='oferta')
]
