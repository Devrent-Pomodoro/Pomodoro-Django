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
            userData.timerLimit = 25
            userData.save()
            return redirect('user')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user(request):
    if request.user.is_anonymous:
        return redirect('home')
    userData = UserData.objects.get(user=request.user)

    context = {
        'timerLimit': userData.timerLimit,
        'totalStudyHour': userData.totalStudyTime//60,
        'totalStudyMinute': userData.totalStudyTime % 60,

    }
    return render(request, 'user.html', context)

def guide(request):
    return render(request, 'guide.html')

def timer(request, timerStyle):
    if request.user.is_anonymous:
        return redirect('home')
    userData = UserData.objects.get(user=request.user)
    timerList = [5 + 10 * i for i in range(1, 1 + userData.timerLimit // 10)]
    context = {'timerList': timerList,}
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
    userData.timerLimit = 25 + (userData.totalStudyTime//10)*10
    userData.save()
    # 60분 추가될 때마다, 설정가능 시간 10분 추가. 기본: 15, 25

    return HttpResponse("data saved!")

def tbd(request):
    return render(request, 'tbd.html')
