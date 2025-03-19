"""
URL configuration for django_tutor project.

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
from django.urls import path
from community.views import articleList, write, viewDetail

app_name = "community" # community : list
urlpatterns = [
    # 커뮤니티와 관련된 경로
    path('write/', write, name='write'),
    path('list/', articleList, name = 'list'),
    path('view_detail/<int:num>/', viewDetail, name = 'view_detail'),
]