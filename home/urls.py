from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),
    path('user', views.tbd, name='user'),
    path('signin', views.tbd, name='signin'),
    path('signup', views.tbd, name='signup'),
    path('guide', views.tbd, name='guide'),
    path('timer', views.tbd),

]