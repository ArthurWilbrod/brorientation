from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return render(request,'accueil/accueilVisiteur.html')

def help(request):
    return render(request,'accueil/help.html')
