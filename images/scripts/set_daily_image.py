from django.core.management.base import BaseCommand
from images.models import Image


class Command(BaseCommand):
    help = "Sets the next daily image by incrementing the current image by one, starting over if necessary."

    def handle(self, *args, **options):
        current_image = Image.objects.filter(is_current_image=True).first()
        print
        next_image = (
            Image.objects.filter(id__gt=current_image.id).order_by("id").first()
        )
        if next_image:
            print(f"Setting {next_image.name} as the daily image.")
            current_image.is_current_image = False
            current_image.save()
            next_image.is_current_image = True
            next_image.save()
        else:
            # If there is no next image, return the first image
            print("Reached the end, starting over.")
            next_image = Image.objects.first()
            print(f"Setting {next_image.name} as the daily image.")
            next_image.is_current_image = True
            next_image.save()


def run():
    command = Command()
    command.handle()
