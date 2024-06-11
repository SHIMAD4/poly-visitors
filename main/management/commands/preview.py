from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Displays a personalized greeting based on the current time"

    def handle(self, *args, **kwargs):
        current_time = timezone.now()
        if 5 <= current_time.hour < 12:
            time_of_day = "morning"
        elif 12 <= current_time.hour < 17:
            time_of_day = "afternoon"
        else:
            time_of_day = "evening"

        self.stdout.write(
            self.style.SUCCESS(
                f"Good {time_of_day}! It's now {current_time.strftime('%X')}"
            )
        )
