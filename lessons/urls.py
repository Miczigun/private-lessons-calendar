from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login-page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register-page'),
    path('profile/<int:pk>', views.profile_page, name='profile-page'),
    path('lesson/<int:pk>', views.lesson_page, name='lesson-page'),
    path('', views.menu_page, name='menu'),
]