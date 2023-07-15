from django.db import models
from django.urls import reverse
from phone_field import PhoneField


class Teacher(models.Model):
    teacher_first_name = models.CharField(max_length=30)
    teacher_last_name = models.CharField(max_length=30)
    seniority = models.IntegerField()

    def __str__(self):
        return self.teacher_first_name


class TeacherProfile(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=200, default=None)

    def __str__(self):
        return f"Student: {self.teacher} Profile. Student's hobby is {self.hobby}"


class Student(models.Model):
    student_first_name = models.CharField(max_length=30)
    student_last_name = models.CharField(max_length=30)
    course = models.IntegerField()
    teacher = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.student_first_name

    def get_absolute_url(self):
        return reverse("academy:student_detail", args=[str(self.id)])


class StudentProfile(models.Model):
    some_student = models.OneToOneField(Student, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=200, default=None)
    religion = models.CharField(max_length=30)
    age = models.IntegerField(default=None)
    birth_date = models.DateField()

    def __str__(self):
        return f"Student: {self.some_student} Profile. Student's hobby is {self.hobby}"


class Subjects(models.Model):
    teacher_name = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student_name = models.ManyToManyField(Student)
    subject_name = models.CharField(max_length=25)
    lecture_amount = models.IntegerField()
    lecture_duration = models.IntegerField()

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse("academy:subject_detail", args=[str(self.id)])
