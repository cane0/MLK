from django.db import models
from users.models import Language, Student, Teacher

class Classroom(models.Model):
    level = models.CharField(max_length=10)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='classroom')

    def __str__(self):
        return f'{self.language.language_name}, level {self.level}'

class TeacherUploadAssignment(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='assignment')
    assignment_title = models.CharField(max_length=100)
    questions_file = models.FileField()
    solutions_file = models.FileField(blank=True)

    def __str__(self):
        return f'{self.assignment_title}'

class StudentUpload(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='student_classroom')
    assignment = models.ForeignKey(TeacherUploadAssignment, on_delete=models.CASCADE, related_name='student_upload')
    answer_file = models.FileField()
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.username} answers to assignment {self.assignment.assigment_title}'