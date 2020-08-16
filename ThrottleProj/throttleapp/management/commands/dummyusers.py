from django.core.management.base import BaseCommand, CommandError
from ...models import UserModel as Member, ActivityPeriodModel
import names
import random


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        # User.objects.create_superuser(username="admin", password="admin", email="admin@gmail.com")
        for number in range(5):
            user_obj = Member(
                User_id='W012A3CD' + str(number),
                real_name=names.get_full_name(),
                tz='America/Los_Angeles',
                status=random.choice(['True', 'False'])
            )
            user_obj.save()
            for i in range(random.choice([1, 2, 3, 4, 5])):
                activity_obj = ActivityPeriodModel(
                    User_id=user_obj,
                    start_time='',
                    end_time='2020-10-25 14:30:59'
                )
                activity_obj.save()
            message = f'Member Added with Name : ' + user_obj.real_name
            self.stdout.write(self.style.SUCCESS(message))
