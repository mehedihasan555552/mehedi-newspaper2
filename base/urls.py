from django.urls import path

from . import views
from .views import LatestPostt,GasAndoilPostt,CriptocurrencyPostt,TechPostt,PostofthedayPostt,Header2Postt,Header1Postt

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', LatestPostt.as_view(), name='latestpost'),
    path('gasandoilpost/<int:pk>/', GasAndoilPostt.as_view(), name='gasandoil'),
    path('cripto/<int:pk>/', CriptocurrencyPostt.as_view(), name='cripto'),
    path('tech/<int:pk>/', TechPostt.as_view(), name='tech'),
    path('postoftheday/<int:pk>/', PostofthedayPostt.as_view(), name='postof'),
    path('header1/<int:pk>/', Header1Postt.as_view(), name='header1'),
    path('header2/<int:pk>/', Header2Postt.as_view(), name='header2'),




    ]
