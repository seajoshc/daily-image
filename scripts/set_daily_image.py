from django.core.management.base import BaseCommand
from images.models import Image


class Command(BaseCommand):
    help = "Sets the next daily image by incrementing the current image by one, starting over if necessary."

    def handle(self, *args, **options):
        current_image = Image.objects.filter(is_current_image=True).first()
        next_image = (
            Image.objects.filter(id__gt=current_image.id).order_by("id").first()
        )
        if next_image:
            return next_image.id
        else:
            # If there is no next image, return the first image
            return Image.objects.first().id
