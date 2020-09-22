from django.shortcuts import render,redirect
from . models import *
from django.views.generic import  DetailView
from django.utils import timezone

# Create your views here.

def index(request):
    l=LatestPost.objects.all().order_by('-date_posted')[:1]
    ll=LatestPost.objects.all().order_by('-date_posted')[1:2]
    lll=LatestPost.objects.all().order_by('date_posted').reverse()[1:3]
    posts=LatestPost.objects.all().order_by('date_posted').reverse()[3:7]
    bb=LatestPost.objects.all().order_by('-date_posted')[:5]
    if request.method == 'GET':
        category=['1']
        gass=LatestPost.objects.order_by('-date_posted').filter(category=category)[:2]

    try:
        if request.method =='GET':
            category=['2']
            p=LatestPost.objects.order_by('-date_posted').filter(category=category)[:2]
    except:
        pass

    try:
        if request.method =='GET':
            category=['3']
            c=LatestPost.objects.order_by('-date_posted').filter(category=category)[:2]
    except:
        pass

    try:
        if request.method =='GET':
            category=['4']
            d=LatestPost.objects.order_by('-date_posted').filter(category=category)[:2]
    except:
        pass


    try:
        if request.method =='GET':
            category=['5']
            e=LatestPost.objects.order_by('-date_posted').filter(category=category)[:2]
    except:
        pass

    try:
        if request.method =='GET':
            video=MEOCHANNEL.objects.all().order_by('-date_posted')[:2]
    except:
        pass



    context={'gass':gass,'p':p,'c':c,'d':d,'e':e,'video':video,'posts':posts,'l':l,'ll':ll,'bb':bb,'lll':lll}
    return render(request, 'base/index.html',context)


def Gas(request):
    category=['1']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'base/gas.html',context)


def MEO(request):
    gass=MEOCHANNEL.objects.all().order_by('-date_posted')
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'base/meo.html',context)


def Cripto(request):
    category=['2']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'base/economy.html',context)


def Enorgy(request):
    category=['3']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'base/enorgy.html',context)


def Tech(request):
    category=['5']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'base/tech.html',context)

class LatestPostt(DetailView):
    model = LatestPost










class MeoPostt(DetailView):
    model = MEOCHANNEL
