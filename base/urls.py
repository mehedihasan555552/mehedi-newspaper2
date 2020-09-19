from django.urls import path

from . import views
from .views import LatestPostt,MeoPostt

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', LatestPostt.as_view(), name='latestpost'),

    path('meo/<int:pk>/', MeoPostt.as_view(), name='meo'),
    path('gas/', views.Gas, name='gas'),
    path('cripto/', views.Cripto, name='cripto'),
    path('enorgy/', views.Enorgy, name='enorgy'),
    path('meo/', views.MEO, name='meo'),
    path('tech/', views.Tech, name='tech'),




    ]
