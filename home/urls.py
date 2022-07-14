from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('user', views.tbd, name='user'),
    path('signin', views.tbd),
    path('signup', views.tbd),
    path('guide', views.tbd),
    path('timer', views.tbd),

]