from django.shortcuts import render
from community.models import Article

# Create your views here.
def dashboard(request):

    return render(request, 'dashboard.html')