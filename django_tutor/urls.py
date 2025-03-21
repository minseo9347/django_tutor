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
from django.contrib import admin
from django.urls import path, include
from django_tutor.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/
    path('', index, name = 'index'),
    path('', include('community.urls')), # 해당 경로에 커뮤니티 앱의 경로를 저장하고 여기에 둔다.
    path('', include('dashboard.urls')),
    # list, write, view_detail
  
    # 유지보수측면에서 name 변수로 지정하면 URL 경로가 변경되더라도 name만 일관되면 템플릿이나 뷰 코드를 수정할 필요가 없다.
# view의 함수 # write/ 패스가 오면 write 함수를 실행하라.
]
