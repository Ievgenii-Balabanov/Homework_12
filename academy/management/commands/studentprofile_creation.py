import random

from django.core.management import BaseCommand
from django.db.models import Max, Min
from django.shortcuts import get_object_or_404
from faker import Faker

from academy.models import Subjects, Teacher, Student, StudentProfile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("new_studentprofile", type=int, help="Add a 'new student profile' ")

    # , choices = range(1, 50)
    def handle(self, *args, **kwargs):

        faker = Faker()
        religion_list = [
            "Christianity",
            "Islam",
            "Catholicism",
            "Hinduism",
            "Buddhism",
            "Sikhism",
            "Protestantism",
            "Judaism",
            "Scientology",
        ]

        hobby_list = [
            "Reading",
            "Martial Arts",
            "Jewelry Making",
            "Woodworking",
            "Gardening",
            "Video Games",
            "Fishing",
            "Walking",
            "Yoga",
            "Traveling",
            "Golf",
            "Writing",
            "Running",
            "Tennis",
            "Dancing",
            "Painting",
            "Cooking",
            "Bicycling",
            "Podcasts",
            "Music",
        ]

        max_id = Student.objects.all().aggregate(max_id=Max("id"))["max_id"]
        min_id = Student.objects.all().aggregate(min_id=Min("id"))["min_id"]
        pk = random.randrange(min_id, max_id)
        particular_student = Student.objects.get(pk=pk)
        StudentProfile.objects.bulk_create(
            (
                StudentProfile(some_student=particular_student, hobby=random.choice(hobby_list),
                               religion=random.choice(religion_list),
                               age=random.randint(17, 33), birth_date=faker.date_of_birth())
                for _ in range(kwargs.get('new_studentprofile'))
            )
        )
        self.stdout.write(self.style.SUCCESS(f"New studentprofile number: {kwargs.get('new_studentprofile')}"))
