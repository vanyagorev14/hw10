import random
import secrets

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand  # , CommandError

from faker import Faker


class Command(BaseCommand):
    help = 'Creates the specified number of new users. You must specify a number in the range [1; 10]'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('new_user', type=int, choices=range(1, 10), help='The passed '
                                                                                                      'value of the '
                                                                                                      'created users')

    def handle(self, *args, **options):
        for j in range(options['new_user']):
            fake = Faker()
            user = User.objects.create(first_name=fake.first_name(), last_name=fake.last_name(),
                                       email=fake.email(), password=secrets.token_urlsafe(32),
                                       username=Faker().name() + str(random.randint(1, 883322)))
            user.save()

            self.stdout.write(self.style.SUCCESS('Successfully added user "%s"' % user.username))