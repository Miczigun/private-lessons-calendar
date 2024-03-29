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
    path('update-lesson/<int:pk>', views.update_lesson, name='update-lesson'),
    path('update-class/<int:pk>', views.update_class, name='update-class'),
    path('delete-lesson/<int:pk>', views.delete_lesson, name='delete-lesson'),
    path('delete-class/<int:pk>', views.delete_class, name='delete-class'),
    path('update-bio/<int:pk>', views.update_bio, name='update-bio'),
    path('', views.menu_page, name='menu'),
]