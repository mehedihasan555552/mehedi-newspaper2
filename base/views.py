from django.shortcuts import render,redirect
from . models import *
from django.views.generic import  DetailView
from django.utils import timezone

# Create your views here.
def index(request):
    posts = LatestPost.objects.all().order_by('-date_posted')
    postoftheday=Post_of_the_day.objects.all()
    music=GasAndOil.objects.all().order_by('-date_posted')
    cripto = Criptocurrency.objects.all().order_by('-date_posted')
    tech = Technology.objects.all().order_by('-date_posted')
    header1 =HeaderPost1.objects.all().order_by('-date_posted')
    header2 = HeaderPost2.objects.all().order_by('-date_posted')
    context={'posts':posts,'postoftheday':postoftheday,'music':music,
    'cripto':cripto,'tech':tech,'header1':header1,'header2':header2,
    }
    return render(request, 'base/index.html',context)


class LatestPostt(DetailView):
    model = LatestPost


class GasAndoilPostt(DetailView):
    model = GasAndOil


class CriptocurrencyPostt(DetailView):
    model = Criptocurrency

class TechPostt(DetailView):
    model = Technology

class PostofthedayPostt(DetailView):
    model = Post_of_the_day

class Header1Postt(DetailView):
    model = HeaderPost1

class Header2Postt(DetailView):
    model = HeaderPost2
