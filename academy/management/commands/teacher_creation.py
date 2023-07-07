import random

from django.core.management import BaseCommand

from faker import Faker

from academy.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("new_teacher", type=int, help="Add a 'new_teacher' ", choices=range(1, 501))

    def handle(self, *args, **kwargs):
        faker = Faker()
        Teacher.objects.bulk_create(
            (
                Teacher(teacher_first_name=faker.first_name(), teacher_last_name=faker.last_name(),
                        seniority=random.randint(1, 40))
                for _ in range(kwargs.get('new_teacher'))
            )
        )
        self.stdout.write(self.style.SUCCESS(f"New Teachers number: {kwargs.get('new_teacher')}"))
