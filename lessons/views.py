from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from .models import User, Topic


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect('menu')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            messages.error("Wrong password!")

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

    topics = Topic.objects.all()
    context = {'topics': topics}

    return render(request, 'lessons/menu.html', context)
