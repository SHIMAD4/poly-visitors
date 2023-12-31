from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Displays a personalized greeting based on the current time'

    def handle(self, *args, **kwargs):
        current_time = timezone.now()
        time_of_day = "morning" if 5 <= current_time.hour < 12 else "afternoon" if 12 <= current_time.hour < 17 else "evening"

        self.stdout.write(self.style.SUCCESS("Good %s! It's now %s" % (time_of_day, current_time.strftime('%X'))))
