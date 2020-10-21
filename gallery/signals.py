import os
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import galleryImages

@receiver(pre_delete, sender=galleryImages)
def delete_gallery_images(sender, instance, **kwargs):
    if instance:
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.image.name))
