# from django.shortcuts import request
from django.http import HttpResponse
from django.shortcuts import render
# ----------------------------------codewithharry video 6,7------------------------------
def homepage(request):
    # return HttpResponse("<h1>Hello home page</h1> <a href='''https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'''>Django CodeWithHarry</a>" )
    # params={'name':'shaan', 'mood': 'django'}
    return render(request, 'home.html')

def removepunc(request):
    # Get the text
    djtext=request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'default')
    print(djtext)
    print(removepunc)
    # analyze the text
    return HttpResponse("removepunc")
   
def capitalizefirst(request):
    return HttpResponse("capfirst")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaeremove <a href='/'> back </a>")
def charcount(request):
    return HttpResponse("charcount")
    

# Create your views here.
