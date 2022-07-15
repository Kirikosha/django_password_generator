from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list(string.ascii_lowercase)
    
    if request.GET.get('uppercase'):
        characters += list(string.ascii_uppercase)
    if request.GET.get('special'):
        characters += list(string.punctuation)
    if request.GET.get('numbers'):
        characters += list(string.digits)
        
    
    length = int(request.GET.get('length', 12))
    
    the_password = ''
    
    for x in range(length):
        the_password += random.choice(characters)
    
    return render(request, 'generator/password.html', {"password": the_password })

def about_creator(request):
    return render(request, 'generator/about_creator.html')