from django.urls import path
from .views import TeacherRegisterView, StudentRegisterView, HomeView, StudentSubjectView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('subject_student/<pk>/', StudentSubjectView.as_view(), name='subject-student'),
    path('teacher_register/', TeacherRegisterView.as_view(), name='teacher-register'),
    path('student_register/', StudentRegisterView.as_view(), name='student-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]