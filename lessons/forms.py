from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from .models import User, Lessons, Classes


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


class ClassesForm(forms.Form):
    phone = PhoneNumberField(region='PL', widget=PhoneNumberPrefixWidget(
        initial='PL',
        country_choices=[
            ('PL', 'Poland'),
            ('US', 'United States')
        ]
    ))
    email = forms.EmailField()
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'