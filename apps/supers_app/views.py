from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from models import *
import re
import bcrypt
def getheropowers(id):
    powerlist = Hero.objects.get(id = id).powers.all()
    plist = ""
    context = {}
    for power in powerlist:
        plist = plist + power.name + ", "
    context['plist'] = plist
    return context
def getlikes(heroid):
    numlikes = Hero.objects.get(id = heroid).liked.count()
    return numlikes
def getHeroList(request):
    herolist = []
    heroes = Hero.objects.all()
    userid = request.session['loggedinuser']
    user = User.objects.get(id = userid)
    for hero in heroes:
        guy = {}
        if user in hero.liked.all():
            guy['liked'] = True
        else:
            guy['liked'] = False
        name = hero.name
        guy['id'] = hero.id
        guy['name'] = name
        stuff = getheropowers(hero.id)
        guy['powers'] = stuff['plist']
        guy['likes'] = getlikes(hero.id)
        herolist.append(guy)
    return herolist

def index(request):
    print "got to supers index func"
    context = {}
    context['herolist'] = getHeroList(request)
    return render(request, 'dashboard.html', context)
def logout(request):
    del request.session['loggedinuser']
    return redirect('/')
def heropage(request):
    return render(request, 'addHero.html')
def addHero(request):
    name = request.POST['hero_name']
    context = {}
    hero, created = Hero.objects.get_or_create(name = name)
    if created == True:
        return redirect('supers/home')
    context['error'] = "{} already exists in the system.".format(name)
    context['herolist'] = getHeroList(request)
    return render(request, 'dashboard.html', context)
def powerspage(request):
    return render(request, 'addPower.html')
def addPower(request):
    name = request.POST['name']
    desc = request.POST['desc']
    context = {}
    power, created = Power.objects.get_or_create(name = name, desc = desc)
    if created == True:
        return redirect('supers/home')
    context['error'] = "{} already exists in the system.".format(name)
    context['herolist'] = getHeroList(request)
    return render(request, 'dashboard.html', context)
def onehero(request, number):
    hero = Hero.objects.get(id = number)
    context = {}
    context['heroid'] = hero.id
    context['name'] = hero.name
    context['likes'] = getlikes(number)
    stuff = getheropowers(hero.id)
    context['powers'] = stuff['plist']
    context['powerlist'] = Power.objects.all()
    return render(request, 'onehero.html', context)
def addheropower(request):
    newpower = Power.objects.get(id = request.POST['poweradded'])
    hero = Hero.objects.get(id = request.POST['hero_id'])
    hero.powers.add(newpower)
    return redirect('supers/home')
def likehero(request, number):
    user1 = User.objects.get(id = request.session['loggedinuser'])
    hero1 = Hero.objects.get(id = number)
    user1.likes.add(hero1)
    return redirect('supers/home')
def unlikehero(request, number):
    user1 = User.objects.get(id = request.session['loggedinuser'])
    hero1 = Hero.objects.get(id = number)
    user1.likes.remove(hero1)
    return redirect('supers/home')
