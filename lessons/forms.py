from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Lessons


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']


class LessonForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

    class Meta:
        model = Lessons
        fields = '__all__'
        exclude = ['teacher']