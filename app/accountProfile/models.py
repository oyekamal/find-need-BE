from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django_countries.fields import CountryField


class Language(models.Model):
    name = models.CharField(max_length=150)
    flag_pictures = models.ImageField(
        upload_to='flag_pictures', blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = CountryField()
    
    def __str__(self):
        return self.name.name

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + " : " + self.country.name.name


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=150)
    languages = models.ManyToManyField(Language)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    profile_picture = models.ImageField(
        upload_to='profile_pictures', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')


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
    
    def get_followers_count(self):
        return self.followers.count()

    def get_following_count(self):
        return self.following.count()
    
class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"