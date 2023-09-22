from django.shortcuts import render
from rest_framework import generics
from lessons.models import User, Topic, Lessons, Classes
from .serializers import UserSerializer, TopicSerializer, LessonsSerializer, ClassesSerializer


class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
