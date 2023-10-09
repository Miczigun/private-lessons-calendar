from django.urls import path
from rest_framework import routers
from .views import (TopicListView, LessonListView, LessonsCreateView,UserRetrieveView,
                    LessonsRetrieveView, ClassesRetrieveView, LessonsUpdateView)


urlpatterns = [
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>', LessonsRetrieveView.as_view(), name='lesson-detail'),
    path('update-lesson/<int:pk>', LessonsUpdateView.as_view(), name='lesson-update'),
    path('create-lesson/', LessonsCreateView.as_view(), name='lesson-create'),
    path('user/<int:pk>', UserRetrieveView.as_view(), name='user-detail'),
    path('class/<int:pk>', ClassesRetrieveView.as_view(), name='class-detail'),
]