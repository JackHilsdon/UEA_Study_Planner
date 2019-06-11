from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('about/', views.about, name='about_page'),
]