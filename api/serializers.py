from rest_framework import serializers
from django.urls import reverse
from lessons.models import User, Topic, Lessons, Classes
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'bio']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()
    teacher = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='teacher_id',
        lookup_url_kwarg='pk')

    class Meta:
        model = Lessons
        fields = '__all__'

    def get_topic(self, obj):
        return obj.topic.name if obj.topic else None


class ClassesSerializer(serializers.ModelSerializer):

    phone = PhoneNumberField(region='PL')

    class Meta:
        model = Classes
        fields = '__all__'


class LessonsRetrieveSerializer(serializers.ModelSerializer):
    topic = serializers.SerializerMethodField()
    classes = ClassesSerializer(many=True, read_only=True)
    teacher = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='teacher_id',
        lookup_url_kwarg='pk')

    class Meta:
        model = Lessons
        fields = '__all__'

    def get_topic(self, obj):
        return obj.topic.name if obj.topic else None

