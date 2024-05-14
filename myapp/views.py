from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os
from myproject.settings import BASE_DIR

def login_page(request):
    print(os.path.join(BASE_DIR, 'static'))
    return render(request, 'index.html')

# Create your views here.
def show_signup(request):
    print(os.path.join(BASE_DIR, 'static'))
    return render(request, 'main.html')