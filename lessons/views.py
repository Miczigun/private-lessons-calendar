from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserForm, LessonForm, ClassesForm
from .models import User, Topic, Lessons, Classes


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
    lessons = Lessons.objects.filter(teacher=user)

    context = {'user': user, 'lessons': lessons }
    return render(request, 'lessons/profile.html', context)


def lesson_page(request, pk):
    lesson = Lessons.objects.get(id=pk)
    classes = Classes.objects.filter(lesson=pk)

    context = {'lesson': lesson, 'classes': classes}

    return render(request, 'lessons/lesson_page.html', context)

@login_required
def create_lesson(request):
    form = LessonForm()

    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.teacher = request.user
            lesson.save()
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            for time in range(8,16):
                for day in days:
                    Classes.objects.create(
                        lesson=lesson,
                        day=day,
                        start_time=f'{time}:00',
                        end_time=f'{time+1}:00',
                    )

            return redirect('profile-page', pk=request.user.id)

    context = {'form': form}
    return render(request, 'lessons/create_lesson.html', context)

@login_required
def your_lesson(request, pk):
    lesson = Lessons.objects.get(id=pk)
    classes = Classes.objects.filter(lesson=pk)

    context = {'lesson': lesson, 'classes': classes}
    return render(request, 'lessons/your_lessons.html', context)


def update_class(request, pk):
    classes = Classes.objects.get(id=pk)
    form = ClassesForm()
    if request.method == "POST":
        form = ClassesForm(request.POST)
        if form.is_valid():
            classes.phone = form.cleaned_data['phone']
            classes.email = form.cleaned_data['email']
            classes.name = form.cleaned_data['name']
            classes.surname = form.cleaned_data['surname']
            classes.booked = True
            classes.save()
            return redirect('lesson-page', pk=classes.lesson.id)

    context = {'form': form}
    return render(request, 'lessons/update_class.html', context)

@login_required
def delete_lesson(request, pk):
    lesson = Lessons.objects.get(id=pk)

    if request.user == lesson.teacher:
        lesson.delete()
        return redirect('profile-page', pk=request.user.id)
    else:
        return HttpResponse("You don't have permission to do that!")

@login_required
def delete_class(request, pk):
    classes = Classes.objects.get(id=pk)

    if request.user == classes.lesson.teacher:
        classes.booked = False
        classes.name = ""
        classes.surname = ""
        classes.email = ""
        classes.phone = ""
        classes.save()
        return redirect('your-lesson', pk=classes.lesson.id)
    else:
        return HttpResponse("You don't have permission to do that!")