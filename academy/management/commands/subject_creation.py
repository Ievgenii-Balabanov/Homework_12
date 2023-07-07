import random

from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from academy.models import Subjects, Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("new_subject", type=int, help="Add a 'new_subject' ", choices=range(1, 20))

    def handle(self, *args, **kwargs):
        subjects_list = [
            'Mathematics',
            'Algebra',
            'Geometry',
            'Science',
            'Geography',
            'History',
            'English',
            'Spanish',
            'German',
            'French',
            'Latin',
            'Greek',
            'Arabic',
            'Computer Science',
            'Art',
            'Economics',
            'Music',
            'Drama',
            'Physical Education',
        ]

        teacher = Teacher.objects.all()
        Subjects.objects.bulk_create(
            (
                Subjects(teacher_name=random.choice(teacher), subject_name=random.choice(subjects_list),
                         lecture_amount=random.randint(1, 100),
                         lecture_duration=random.randint(1, 3))
                for _ in range(kwargs.get('new_subject'))
            )
        )
        self.stdout.write(self.style.SUCCESS(f"New Subjects number: {kwargs.get('new_subject')}"))
