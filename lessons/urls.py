from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register-page'),
    path('profile/<int:pk>', views.profile_page, name='profile-page'),
    path('lesson/<int:pk>', views.lesson_page, name='lesson-page'),
    path('your-lesson/<int:pk>', views.your_lesson, name='your-lesson'),
    path('create-lesson/', views.create_lesson, name='create-lesson'),
    path('update-class/<int:pk>', views.update_class, name='update-class'),
    path('delete-lesson/<int:pk>', views.delete_lesson, name='delete-lesson'),

    path('', views.menu_page, name='menu'),
]