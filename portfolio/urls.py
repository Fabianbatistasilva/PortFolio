
from django.urls import path
from portfolio.views import *

urlpatterns = [
   path('', home , name='home'),
   path('sobre_Fabian/', sobre , name='sobre'),
   path('oferta/', oferta , name='oferta'),
]
