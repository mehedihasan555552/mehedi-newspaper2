from django.shortcuts import render
from arobic. models import *
from django.views.generic import  DetailView
from django.utils import timezone

# Create your views here.

def arindex(request):
    header=[]
    l=LatestPost.objects.filter(header=True).order_by('-date_posted')[:1]
    ll=LatestPost.objects.all().order_by('-date_posted')[1:2]
    lll=LatestPost.objects.filter(header=True).order_by('date_posted').reverse()[1:3]
    posts=LatestPost.objects.all().order_by('date_posted').reverse()[:4]
    bb=LatestPost.objects.all().order_by('-date_posted')[:5]
    video1=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]
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

    # try:
    #     if request.method =='GET':
    #         l=LatestPost.objects.filter(LatestPost.header==True).order_by('-date_posted')[:1]
    # except:
    #     pass

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



    context={'gass':gass,'p':p,'c':c,'e':e,'video':video,'posts':posts,'l':l,'ll':ll,'bb':bb,'lll':lll,'video1':video1}
    return render(request, 'arobic/index1.html',context)


def arGas(request):
    category=['1']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'arobic/gas.html',context)


def arMEO(request):
    gass=MEOCHANNEL.objects.all().order_by('-date_posted')
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'arobic/meo.html',context)


def arCripto(request):
    category=['2']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'arobic/economy.html',context)


def arEnorgy(request):
    category=['3']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'arobic/enorgy.html',context)


def arTech(request):
    category=['5']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    video=MEOCHANNEL.objects.all().order_by('-date_posted')[:1]

    context={'gass':gass,'video':video}
    return render(request, 'arobic/tech.html',context)

class arLatestPostt(DetailView):
    model = LatestPost










class arMeoPostt(DetailView):
    model = MEOCHANNEL
