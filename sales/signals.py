import os
from django.conf import settings
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import VehicleImages

@receiver(pre_delete, sender=VehicleImages)
def delete_vehicle_images(sender, instance, **kwargs):
    if instance:
        os.remove(os.path.join(settings.MEDIA_ROOT, instance.image.name))
