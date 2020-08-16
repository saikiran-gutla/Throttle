from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        User.objects.create_superuser(username="admin", password="admin", email="admin@gmail.com")
        self.stdout.write(self.style.SUCCESS("SuperUser Created"))
