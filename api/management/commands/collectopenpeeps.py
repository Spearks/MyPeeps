from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core.files import File
from django.contrib.staticfiles.storage import staticfiles_storage

import os

OPENPEEPS_PATH = settings.OPENPEEPS_PATH

class Command(BaseCommand):
    help = "Sends the OpeenPeeps file to the Backblaze B2 bucket. Configure the relative path in OPEENPEEPS_PATH in settings.py"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Starting OpeenPeeps upload..."))
        self.stdout.write(self.style.SUCCESS("OpeenPeeps path: " + OPENPEEPS_PATH))

        for dirpath, dirnames, filenames in os.walk(OPENPEEPS_PATH):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as f:
                    file = File(f)
                    name = os.path.join('openpeeps', file_path.replace(OPENPEEPS_PATH, ''))
                    staticfiles_storage.save(name, file)

        self.stdout.write(self.style.SUCCESS("Finished uploading OpeenPeeps."))