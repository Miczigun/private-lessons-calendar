from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from .models import User
# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect('menu')

    if request.method == "POST":
        username = request.POST.get('login')
        password = request.POST.get('password')

        # try:
        #     user = User.get.object()

    return render(request, 'lessons/login_page.html')


def register_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')

    return render(request, 'lessons/register_page.html', {'form': form})

def menu_page(request):
    return render(request, 'lessons/menu')