from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return redirect('user')
    return render(request, 'home.html')

def tbd(request):
    return HttpResponse("to be done...")
