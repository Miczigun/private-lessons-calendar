from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from lessons.models import User, Topic, Lessons, Classes
from .serializers import UserSerializer, TopicSerializer, LessonsSerializer, ClassesSerializer


class TopicListView(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class LessonDetail(viewsets.ReadOnlyModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsCreateView(generics.CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
        lesson = Lessons.objects.get(pk=serializer.data['id'])
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for time in range(8, 16):
            for day in days:
                Classes.objects.create(
                    lesson=lesson,
                    day=day,
                    start_time=f'{time}:00',
                    end_time=f'{time + 1}:00',
                )
