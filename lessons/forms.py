from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.validators import validate_international_phonenumber
from .models import User, Lessons


# Create a form for user registration
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username']


# Create a form for lessons
class LessonForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS class 'form-control my-2' to visible fields for bootstrap styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

    class Meta:
        model = Lessons
        fields = '__all__'
        # Exclude the 'teacher' field from the form because teacher field is set by request.user
        exclude = ['teacher']


# Create a form for booking classes using forms.Form because phone field have to be define by phonenumbers library
class ClassesForm(forms.Form):

    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = PhoneNumberField(region='PL', widget=PhoneNumberPrefixWidget(
        initial='PL',
        country_choices=[
            ('PL', 'Poland'),
            ('US', 'United States')
        ]
    ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS class 'form-control my-2' to visible fields for bootstrap styling
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'
