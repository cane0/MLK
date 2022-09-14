from msilib.schema import ListView
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from numpy import save
from .forms import TeacherSignUpForm, StudentSignUpForm
from .models import User, Teacher, Student, Language
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class TeacherRegisterView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account has been created successfully"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.language = form.cleaned_data.get('language')
        teacher.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Teacher Signup Page'
        context['user_type'] = 'Teacher'
        return context

class StudentRegisterView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    success_message = "Your account has been created successfully"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.language = form.cleaned_data.get('language')
        student.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student Signup Page'
        context['user_type'] = 'Student'
        return context

class HomeView(LoginRequiredMixin, ListView):
    model = Student
    template_name = 'users/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.filter(user=self.request.user).first()
        context['teacher'] = Teacher.objects.filter(user=self.request.user).first()
        return context

class StudentSubjectView(DetailView):
    model = Language
    template_name = 'users/language_student.html'
    
    def get_context_data(self, **kwargs):
        context = super(StudentSubjectView, self).get_context_data(**kwargs)
        language = Language.objects.filter(language_name=self.object.language_name).first().language_name
        return context
