from django.http import HttpResponse
from django.shortcuts import render
import string

def homepage(request):
    return render(request, 'home.html')  

def removepunc(request):
    djtext = request.GET.get('text', '')
    cleaned = djtext.translate(str.maketrans('', '', string.punctuation))
    return render(request, 'home.html', {'result': cleaned, 'operation': 'Remove Punctuation'})

def capitalizefirst(request):
    djtext = request.GET.get('text', '')
    cleaned = djtext.title()             
    return render(request, 'home.html', {'result': cleaned})

def newlineremove(request):
    djtext = request.GET.get('text', '')
    cleaned = djtext.replace('\n', ' ')  
    return render(request, 'home.html', {'result': cleaned})

def spaceremove(request):
    djtext = request.GET.get('text', '')
    cleaned = ' '.join(djtext.split())   
    return render(request, 'home.html', {'result': cleaned})

def charcount(request):
    djtext = request.GET.get('text', '')
    count = len(djtext)
    return render(request, 'home.html', {'result': count})

