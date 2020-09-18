from django.shortcuts import render,redirect
from . models import *
from django.views.generic import  DetailView
from django.utils import timezone

# Create your views here.

def index(request):
    l=LatestPost.objects.all().order_by('-date_posted')[:1]
    ll=LatestPost.objects.all().order_by('-date_posted')[::-3]
    posts=LatestPost.objects.all().order_by('-date_posted')[:2]
    bb=LatestPost.objects.all().order_by('-date_posted')[:5]
    if request.method == 'GET':
        category=['1']
        gass=LatestPost.objects.order_by('-date_posted').filter(category=category)

    try:
        if request.method =='GET':
            category=['2']
            p=LatestPost.objects.order_by('-date_posted').filter(category=category)
    except:
        pass

    try:
        if request.method =='GET':
            category=['3']
            c=LatestPost.objects.order_by('-date_posted').filter(category=category)
    except:
        pass

    try:
        if request.method =='GET':
            category=['4']
            d=LatestPost.objects.order_by('-date_posted').filter(category=category)
    except:
        pass


    try:
        if request.method =='GET':
            category=['5']
            e=LatestPost.objects.order_by('-date_posted').filter(category=category)
    except:
        pass

    try:
        if request.method =='GET':
            video=MEOCHANNEL.objects.all().order_by('-date_posted')
    except:
        pass



    context={'gass':gass,'p':p,'c':c,'d':d,'e':e,'video':video,'posts':posts,'l':l,'ll':ll,'bb':bb}
    return render(request, 'base/index.html',context)


def Gas(request):
    category=['1']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    w =GasAndOil.objects.order_by('-date_posted').filter(category=category)
    p =Criptocurrency.objects.order_by('-date_posted').filter(category=category)
    x =Technology.objects.order_by('-date_posted').filter(category=category)
    y =Post_of_the_day.objects.order_by('-date_posted').filter(category=category)
    posts = LatestPost.objects.all().order_by('-date_posted')
    context={'gass':gass,'w':w,'p':p,'x':x,'y':y,'posts':posts}
    return render(request, 'base/gas.html',context)


def Cripto(request):
    category=['2'] or ['3']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    w =GasAndOil.objects.order_by('-date_posted').filter(category=category)
    p =Criptocurrency.objects.order_by('-date_posted').filter(category=category)
    x =Technology.objects.order_by('-date_posted').filter(category=category)
    y =Post_of_the_day.objects.order_by('-date_posted').filter(category=category)
    posts = LatestPost.objects.all().order_by('-date_posted')
    context={'gass':gass,'w':w,'p':p,'x':x,'y':y,'posts':posts}
    return render(request, 'base/cripto.html',context)


def Tech(request):
    category=['5']
    gass=LatestPost.objects.order_by('-date_posted').filter(category=category)
    w =GasAndOil.objects.order_by('-date_posted').filter(category=category)
    p =Criptocurrency.objects.order_by('-date_posted').filter(category=category)
    x =Technology.objects.order_by('-date_posted').filter(category=category)
    y =Post_of_the_day.objects.order_by('-date_posted').filter(category=category)
    posts = LatestPost.objects.all().order_by('-date_posted')
    context={'gass':gass,'w':w,'p':p,'x':x,'y':y,'posts':posts}
    return render(request, 'base/tech.html',context)

class LatestPostt(DetailView):
    model = LatestPost





class MeoPostt(DetailView):
    model = MEOCHANNEL
