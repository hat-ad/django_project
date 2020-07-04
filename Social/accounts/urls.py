from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('users', views.users_list, name='users'),
    path('otherprof/<str:id>', views.other_prof, name='otherprof'),

]

