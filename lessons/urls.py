from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login-page'),
    path('register/', views.register_page, name='register-page'),
]