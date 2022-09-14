from distutils.command.upload import upload
import email
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.utils.text import slugify
from django.conf import settings

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

class Language(models.Model):
    language_name = models.SlugField(max_length=100)
    language_description = models.TextField(default='Une langue au Cameroun')
    language_image = models.ImageField(upload_to='language_images')

    def __str__(self):
        return self.language_name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, related_name="teacher")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Teacher {self.user.username}'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language, related_name='students')

    def __str__(self):
        return f'Student {self.user.username}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='booty.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'