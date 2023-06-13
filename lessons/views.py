from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.


def login(request):
    return render(request, 'lessons/login_page.html')

def register_page(request):
    form = UserForm()

    return render(request, 'lessons/register_page.html', {'form':form})