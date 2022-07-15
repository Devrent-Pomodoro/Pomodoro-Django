from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .models import StudyTime, UserData
import logging
logger = logging.getLogger('django')

def home(request):
    if request.user.is_authenticated:
        return redirect('user')
    return render(request, 'home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('user')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            userAuth = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, userAuth)  # 로그인

            # 사용자 관련 정보 추가하기
            userData = UserData()
            userData.user = userAuth
            userData.totalStudyTime = 0
            userData.timerLimit = 0
            userData.save()
            return redirect('user')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user(request):
    if request.user.is_anonymous:
        return redirect('home')
    context = {
        'timerLimit':30,
        'totalStudyHour': 11,
        'totalStudyMinute': 12,
    }
    return render(request, 'user.html', context)

def guide(request):
    return render(request, 'guide.html')

def timer(request, timerStyle):
    context={}
    if(timerStyle == "clock-and-number"):
        context["showTimerNumber"]= True
    else:
        context["showTimerNumber"] = False
    return render(request, 'timer.html', context)

def saveTime(request):
    studiedMinute = int(request.POST.get('studiedTime'))

    # userData = UserData.objects.get(user=request.user.id)
    userData = UserData.objects.get(user=request.user)
    userData.totalStudyTime += studiedMinute
    userData.save()
    return HttpResponse("data saved!")

def tbd(request):
    return render(request, 'tbd.html')
