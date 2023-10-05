from django.urls import path
from rest_framework import routers
from .views import TopicListView, LessonDetail, LessonsCreateView, UserRetrieveView

router = routers.DefaultRouter()
router.register(r'lessons', LessonDetail)

urlpatterns = router.urls

urlpatterns += [
    path('topics/', TopicListView.as_view(), name='topic-list'),
    path('create-lesson/', LessonsCreateView.as_view(), name='lesson-create'),
    path('user/<int:pk>', UserRetrieveView.as_view(), name='user-detail'),
]