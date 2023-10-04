from rest_framework import serializers
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
    class Meta:
        model = Lessons
        fields = '__all__'


class ClassesSerializer(serializers.ModelSerializer):

    phone = PhoneNumberField(region='PL')

    class Meta:
        model = Classes
        fields = '__all__'
