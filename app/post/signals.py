from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from .models import ImageGroup
from django.utils import timezone
from datetime import timedelta
from .models import BoostRequest

# Assuming the models are defined in the same file or imported correctly


@receiver(post_save, sender=ImageGroup)
def set_image_group_index(sender, instance, created, **kwargs):
    if created:  # Only act on newly created instances
        # Find the highest index value for the group
        max_index = ImageGroup.objects.filter(group_name=instance.group_name).aggregate(
            models.Max("index")
        )["index__max"]

        if max_index is None:  # If it's the first entry in the group
            instance.index = 1
        else:  # If there are existing entries, increment the index
            instance.index = max_index + 1

        instance.save()  # Save the instance with the updated index


@receiver(post_save, sender=BoostRequest)
def update_post_expiration(sender, instance, **kwargs):
    if instance.status == "APPROVED" and instance.boost_package:
        # Calculate the new expiration date
        new_expiration_date = timezone.now() + timedelta(
            days=instance.boost_package.duration_days
        )

        # Update the expiration date of the related Post
        instance.post.expiration_date = new_expiration_date
        instance.post.boost_package = instance.boost_package
        instance.post.save()
