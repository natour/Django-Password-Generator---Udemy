from django.shortcuts import render
import random

# Create your views here.


def home(request):

    return render(request, 'generator/home.html')


def about(request):

    return render(request, 'generator/about.html')


def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('UpperCase'):
        characters.extend('ABCDEFGHIJKLMOPQRSTUVWXYZ')
    if request.GET.get('SpecialChar'):
        characters.extend('!@#$%^&*_')

    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
