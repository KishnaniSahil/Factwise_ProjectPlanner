"""
URL configuration for manageusers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from manageusersapp.views import *
urlpatterns = [
    path('admin/',admin.site.urls),
    path('create_user/', create_user, name='create_user'),
    path('list_users/', list_users, name='list_users'),
    path('describe_user/', describe_user, name='describe_user'),
    path('update_user/', update_user, name='update_user'),
    path('get_user_teams/', get_user_teams, name='get_user_teams'),
    path('create_team/', create_team, name='create_team'),
    path('list_teams/', list_teams, name='list_teams'),
    path('describe_team/', describe_team, name='describe_team'),
    path('update_team/', update_team, name='update_team'),
    path('add_users_to_team/', add_users_to_team, name='add_users_to_team'),
    path('list_team_users/', list_team_users, name='list_team_users'),
    path('create_board/', create_board, name='create_board'),
    path('add_task/', add_task, name='add_task'),
    path('update_task_status/', update_task_status, name='update_task_status'),
    path('list_boards/', list_boards, name='list_boards'),
    path('export_board/', export_board, name='export_board'),
    path('',home,name="home"),
    path('success_page/',success_page,name="success_page"),
    path('admin/', admin.site.urls),
]
