""" Developer note
    - This module defines the Django command `fetch_all` which is run in terminal by: `python manage.py fetch_all`.
      This command is defined in the `Command.handle()` method
"""


from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command


class Command(BaseCommand):
    help = "Runs all fetch commands in the correct order: Entities, Variables, (Parameters - TODO)"

    def handle(self, *args, **options):
        call_command("fetch_entities")
        call_command("fetch_variables")
