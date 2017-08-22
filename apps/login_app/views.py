from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from models import *
import re
import bcrypt

def index(request):
    print "got here first"
    return render(request, 'index.html')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    errors = ""
    context = {}
    try:
        user1 = User.objects.get(email_address=email)
    except ObjectDoesNotExist:
        context['lerrors'] = "Email address is not associated with a login"
        return render(request, 'index.html', context)
    if not bcrypt.checkpw(password.encode(), user1.password.encode()):
        context['lerrors'] = "Password is incorrect"
        return render(request, 'index.html', context)
    context['user'] = user1
    request.session['loggedinuser'] = user1.id
    return redirect('supers/home')

def register(request):
    print "got to here"
    name = request.POST['name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    errors = ""
    context = {}
    # if User.objects.get(email_address = email):
    #     context['errors'] = "This user already exists"
    #     return render(request, 'index.html', context)
    if not User.objects.isEntered(name, 2) :
        errors = errors + " Name must be at least 2 characters and all letters."
    elif not User.objects.isName(name):
        errors = errors + " Name must be at least 2 characters and all letters."
    if not User.objects.isEntered(email, 5):
        errors = errors + " Email must be entered in a correct format (name@domain.com)."
    elif not User.objects.isEmail(email):
        errors = errors + " Email must be entered in a correct format (name@domain.com)."
    if not User.objects.isEntered(password1, 8):
        errors = errors + " Password must have at least 8 characters."
    if password1 != password2:
        errors = errors + " Password and Verify Password must match."
    if errors == "":
        hash1 = bcrypt.hashpw(password1.encode(), bcrypt.gensalt())
        newuser = User.objects.create(name = name,  email_address = email, password= hash1)
        request.session['loggedinuser'] = newuser.id
        return redirect('/supers/home')
    context['errors'] = errors
    return render(request, 'index.html', context)

def logout(request):
    del request.session['loggedinuser']
    return redirect('/')
