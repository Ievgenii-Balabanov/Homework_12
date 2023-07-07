# Generated by Django 4.0 on 2023-07-07 08:58

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=30)),
                ('student_last_name', models.CharField(max_length=30)),
                ('course', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_first_name', models.CharField(max_length=30)),
                ('teacher_last_name', models.CharField(max_length=30)),
                ('seniority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(default=None, max_length=200)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academy.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=25)),
                ('lecture_amount', models.IntegerField()),
                ('lecture_duration', models.IntegerField()),
                ('student_name', models.ManyToManyField(to='academy.Student')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobby', models.CharField(default=None, max_length=200)),
                ('religion', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=None)),
                ('phone_number', phone_field.models.PhoneField(max_length=31)),
                ('birth_date', models.DateField()),
                ('some_student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academy.student')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(to='academy.Teacher'),
        ),
    ]
