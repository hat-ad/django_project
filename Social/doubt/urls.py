from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage,name='Home'),
    path('about', views.about, name='about'),
    path('contact', views.contacts, name='contact'),
    path('doubt', views.doubt, name='doubt'),
    path('doubt_view/<str:slug>', views.doubt_view, name='doubt view'),
    path('comment',views.answers,name='comment'),
    path('search',views.search,name='search'),
]
