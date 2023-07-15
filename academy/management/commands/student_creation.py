import random

from django.core.management import BaseCommand

from faker import Faker

from academy.models import Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("new_student", type=int, help="Add a 'new_student' ", choices=range(1, 501))

    def handle(self, *args, **kwargs):
        faker = Faker()
        Student.objects.bulk_create(
            (
                Student(
                    student_first_name=faker.first_name(),
                    student_last_name=faker.last_name(),
                    course=random.randint(1, 6),
                )
                for _ in range(kwargs.get("new_student"))
            )
        )
        self.stdout.write(self.style.SUCCESS(f"New students number: {kwargs.get('new_student')}"))
