
from django.urls import path

from . import views
from .views import arLatestPostt,arMeoPostt



app_name = 'arobic'

urlpatterns = [
path('', views.arindex, name='arindex'),
path('ar/post/<int:pk>/', arLatestPostt.as_view(), name='arlatestpost'),

path('ar/meo/<int:pk>/', arMeoPostt.as_view(), name='armeo'),
path('ar/gas/', views.arGas, name='argas'),
path('ar/cripto/', views.arCripto, name='arcripto'),
path('ar/enorgy/', views.arEnorgy, name='arenorgy'),
path('ar/meo/', views.arMEO, name='armeo'),
path('ar/tech/', views.arTech, name='artech'),

]
