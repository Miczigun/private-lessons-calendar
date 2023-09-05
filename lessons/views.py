from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from .forms import UserForm
from .models import User, Topic, Lessons


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

def logout_user(request):
    logout(request)
    return redirect('login-page')


def register_page(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')

    return render(request, 'lessons/register_page.html', {'form': form})


def menu_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    lessons = Lessons.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    context = {'topics': topics, 'lessons': lessons}

    return render(request, 'lessons/menu.html', context)

def profile_page(request, pk):
    user = User.objects.get(id=pk)
    lessons = Lessons.objects.get(teacher=user)

    context = {'user':user, 'lessons':lessons }
    return render(request, 'lessons/profile.html', context)
