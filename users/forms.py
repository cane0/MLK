from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Teacher, Language, Profile

class StudentSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    languages = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        widget=forms.Select
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone_number',
            'languages'
        ]

class TeacherSignUpForm(UserCreationForm):
    phone_number = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        widget = forms.Select
    )
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone_number',
            'language'
        ]

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']