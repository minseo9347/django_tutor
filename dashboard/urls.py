from django.urls import path

from dashboard.views import dashboard


app_name = "dashboard" 
urlpatterns = [
    # 커뮤니티와 관련된 경로
    path('dashboard', dashboard, name='dashboard'),
]