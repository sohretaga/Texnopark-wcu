from cmath import log
from hashlib import new
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Contact, News, Project
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError



# Create your views here.

def index(request):
  # news section
  news = News.objects.all().order_by('?')[:6]

  # projects section
  projects = Project.objects.filter(finish=True).order_by('?')[:3]

  #contact section
  fullname = request.POST.get('fullname')
  number = request.POST.get('number')
  email = request.POST.get('email')
  message = request.POST.get('message')

  if request.method == 'POST':
    newMessage = Contact(fullname=fullname, number=number, email=email, message=message)
    newMessage.save()
    messages.add_message(request, messages.INFO, 'Sizinlə qısa zamanda əlaqə saxlayacağıq.')
    return redirect('index')
  
  context = {'news': news, 'projects': projects}
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def signup(request):
  first_name = request.POST.get('first_name')
  last_name = request.POST.get('last_name')
  email = request.POST.get('email')
  password = request.POST.get('password')
  password2 = request.POST.get('password2')

  try:
    if request.method == 'POST':
      if password == password2:
        newUser = User.objects.create_user(first_name = first_name, last_name=last_name, email=email, username=email)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        return redirect('index')
      else:
        messages.add_message(request, messages.INFO, 'Şifrələr eyni deyil!')
        return render(request, 'signup.html')
  except IntegrityError:
    messages.add_message(request, messages.INFO, 'Bu epoçt artıq istifadə olunur!')
    return render(request, 'signup.html')
  return render(request, 'signup.html')

def signin(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, username=email, password=password)
    if user is not None:
      login(request, user)
      return redirect('index')
    else:
      messages.add_message(request, messages.INFO, 'Şifrə vəya mail yanlışdır!')
      return redirect('sign-in')
  return render(request, 'signin.html')

@login_required(login_url='/sign-in/')
def signout(request):
  logout(request)
  return redirect('index')

def contact(request):
  fullname = request.POST.get('fullname')
  number = request.POST.get('number')
  email = request.POST.get('email')
  message = request.POST.get('message')

  if request.method == 'POST':
    newMessage = Contact(fullname=fullname, number=number, email=email, message=message)
    newMessage.save()
    messages.add_message(request, messages.INFO, 'Sizinlə qısa zamanda əlaqə saxlayacağıq.')
    return redirect('index')
  return render(request, 'contact.html')

def news(request):
  news = News.objects.all().order_by('-date')
  context = {'news': news}
  return render(request, 'news.html', context)
  
def newsDetail(request, id):
  news = get_object_or_404(News, id=id)
  context = {'news': news}
  return render(request, 'newsDetail.html', context)

def projects(request):
  if 'continuing' in request.path:
    projects = Project.objects.filter(finish=False).order_by('-date')
    context = {'projects': projects}
    return render(request, 'projects.html', context)
  else:
    projects = Project.objects.filter(finish=True).order_by('-date')
    context = {'projects': projects}
    return render(request, 'projects.html', context)
  
def projectDetail(request, id):
  project = get_object_or_404(Project, id=id)
  context = {'project': project}
  return render(request, 'projectDetail.html', context)


