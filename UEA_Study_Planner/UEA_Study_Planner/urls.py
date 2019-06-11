"""UEA_Study_Planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as authorisation_views
from django.urls import path, include
from users import views as user_views
from users.views import ToDoListView, ToDoDetailView, ToDoCreateView, ToDoUpdateView, ToDoDeleteView, semester_upload



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.registerNewAcc, name="register"),
    path('login/', authorisation_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', authorisation_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('todo/', ToDoListView.as_view(), name="todo"),
    path('todo/<int:pk>/', ToDoDetailView.as_view(), name="todo_detail"),
    path('todo/new/', ToDoCreateView.as_view(), name="todo_create"),
    path('todo/<int:pk>/update/', ToDoUpdateView.as_view(), name="todo_update"),
    path('todo/<int:pk>/delete/', ToDoDeleteView.as_view(), name="todo_delete"),
    path('', include('home_page.urls')),
    path('upload_csv/', semester_upload, name="semester_upload")
]
