from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image


class Language(models.Model):
    name = models.CharField(max_length=150)
    flag_pictures = models.ImageField(
        upload_to='flag_pictures', blank=True, null=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=150)
    languages = models.ManyToManyField(Language)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_picture:
            image = Image.open(self.profile_picture.path)
            # Resize the image using Pillow
            # Adjust the dimensions as per your requirement
            image.thumbnail((300, 300))
            image.save(self.profile_picture.path)

    def __str__(self):
        return self.username
