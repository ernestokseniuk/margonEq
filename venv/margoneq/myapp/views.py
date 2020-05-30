#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
import datetime
from . import models
from . import codegen
from . import forms
from myapp.forms import UserForm, UserProfileInfoForm, AddItemForm, AddCommentForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    context = models.customItem.objects.order_by("-pub_date")
    return render(request,'index.html', context={"customitems":context})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    verifCodeAlert = False
    try:
        code = models.verifyCodes.objects.all().filter(inUse=False)[0]
    except:
        return HttpResponse("Ilość kont wyczerpana")
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        margonemAccountCheck = codegen.checkCode(code.code, request.POST.get("mprofile"))
        if user_form.is_valid() and profile_form.is_valid() and margonemAccountCheck == True:
            user = user_form.save()
            user.set_password(user.password)
            profile = profile_form.save(commit=False)
            profile.verifCode = code
            code.inUse = True
            code.save()
            registered = True
            user.save()
            profile.user = user
            profile.save()
            user = authenticate(username = user.username, password = user.password)
            return HttpResponseRedirect(reverse('user_login'))

        else:

            registerAlert = dict()
            try:
                if profile_form.errors['mprofile']:
                    registerAlert.update({'Podano błędny, lub zajęty link do profilu margonem': "Validmprofile"})
            except:
                if margonemAccountCheck == False:
                    registerAlert.update({'Nie znaleziono kodu weryfikacyjnego na profilu margonem': "validCode"})
            try:
                if user_form.errors['username']:
                    registerAlert.update({'Login najprawdopodobniej jest zajęty': "validLogin"})
            except:
                pass
            try:
                if user_form.errors['password']:
                    registerAlert.update({'Hasło jest zbyt słabe': "validpassword"})
            except:
                pass
            print(user_form.errors.keys())
            user_form = UserForm()
            profile_form = UserProfileInfoForm()
            return render(request, 'registration.html', context={'user_form': user_form,
                                                                 'profile_form': profile_form,
                                                                 'registered': registered,
                                                                 'verCode': code.code,
                                                                 'alerts': registerAlert})
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',context={'user_form':user_form,
                                                        'profile_form':profile_form,
                                                        'registered':registered,
                                                        'verCode':code.code,
                                                        'verifCodeAlert':verifCodeAlert})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return  HttpResponse("Konto nieaktywne")
        else:
            print("Username: {} password {}".format(username,password))
            failed = True
            return render(request,'login.html',context={"failed":failed})
    else:
        return render(request,'login.html')

def addItem(request):
    if request.method == 'POST':
        formm = AddItemForm(data = request.POST)
        if formm.is_valid():
            formm = formm.save(commit=False)
            formm.author = request.user
            formm.save()
            return HttpResponseRedirect(reverse('index'))
        else:
           print(formm.errors)
    else:
        formm = AddItemForm()
    print(request)
    return  render(request,'addItem.html', context={"formm":formm})

def itemView(request, itemid):
    item = models.customItem.objects.get(id=itemid)
    comments = models.Comments.objects.all().filter(topic = item).order_by("pub_date")
    if request.method == 'POST':
        form = AddCommentForm(data=request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.topic = item
            form.author = request.user
            form.save()
            form = AddCommentForm()
            return HttpResponseRedirect(reverse('myapp:itemdet',args=(itemid,)))

        else:
            print(form.errors)
    else:
        form = AddCommentForm()
    return render(request,'itemDet.html', context={"item":item,"form":form,"comments":comments})

def userView(request, userid):
    items = models.customItem.objects.all().filter(author_id = userid).order_by("-pub_date")
    posts = len(items)
    comments = len(models.Comments.objects.all().filter(author_id=userid, deleted=False))
    userinfo = User.objects.get(id=userid)

    return render(request,"userView.html", context={"customitems":items,"posts":posts,"userinfo":userinfo,"comments":comments,})

def itemDel(request,itemid):
    if request.POST:
        print(request.POST)
        commnetId = request.POST.get("comToDel")
        comment = models.Comments.objects.get(id=commnetId)
        if comment.author == request.user:
            comment.deleted = True
            comment.save()
            return HttpResponseRedirect(reverse('myapp:itemdet', args=(itemid,)))
        else:
            return HttpResponseRedirect(reverse('myapp:itemdet', args=(itemid,)))
    else:
        return HttpResponseRedirect(reverse('myapp:itemdet', args=(itemid,)))
