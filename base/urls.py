from django.urls import path

from . import views
from .views import LatestPostt,GasAndoilPostt,CriptocurrencyPostt,TechPostt,PostofthedayPostt,Header2Postt,Header1Postt,CurrencyPostt,MeoPostt

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', LatestPostt.as_view(), name='latestpost'),
    path('gasandoilpost/<int:pk>/', GasAndoilPostt.as_view(), name='gasandoil'),
    path('cripto/<int:pk>/', CriptocurrencyPostt.as_view(), name='cripto'),
    path('currency/<int:pk>/', CurrencyPostt.as_view(), name='currency'),
    path('tech/<int:pk>/', TechPostt.as_view(), name='tech'),
    path('postoftheday/<int:pk>/', PostofthedayPostt.as_view(), name='postof'),
    path('header1/<int:pk>/', Header1Postt.as_view(), name='header1'),
    path('header2/<int:pk>/', Header2Postt.as_view(), name='header2'),
    path('meo/<int:pk>/', MeoPostt.as_view(), name='meo'),
    path('gas/', views.Gas, name='gas'),
    path('cripto/', views.Cripto, name='cripto'),
    path('tech/', views.Tech, name='tech'),




    ]
