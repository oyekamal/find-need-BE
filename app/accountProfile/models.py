from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

# from django_countries.fields import CountryField


class Language(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="flag_pictures", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="flag_pictures", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="flag_pictures", blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " : " + self.country.name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True)
    languages = models.ManyToManyField(Language, blank=True, null=True)

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True, null=True
    )
    profile_picture = models.ImageField(
        upload_to="profile_pictures", blank=True, null=True
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.CharField(max_length=2505, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    tokens = models.TextField(blank=True, null=True)
    is_online = models.BooleanField(default=False, null=True, blank=True)
    last_active = models.DateTimeField(null=True, blank=True)

    # followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # Removed 'email' from REQUIRED_FIELDS

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


class Follow(models.Model):
    follower = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="following"
    )
    following = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="followers"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("follower", "following")


class ChatMessage(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    message = models.TextField()
    image = models.ImageField(upload_to="normal_chat", blank=True, null=True)
    file = models.FileField(
        upload_to="normal_chat/file", blank=True, null=True
    )  # Audio file field
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ["-timestamp"]  # Order by created_at in ascending order

    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"


class Block(models.Model):
    blocker = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="blocking"
    )
    blocked = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="blocked_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            "blocker",
            "blocked",
        )


class Notification(models.Model):
    # List of tokens
    token = models.TextField(help_text="JSON-encoded list of tokens")

    # Notification type
    NOTIFICATION_TYPE_CHOICES = [
        ("info", "Information"),
        ("warning", "Warning"),
        ("alert", "Alert"),
        # Add other types as needed
    ]
    notification_type = models.CharField(
        max_length=20, choices=NOTIFICATION_TYPE_CHOICES, blank=True, null=True
    )

    # Title
    title = models.CharField(max_length=255, blank=True, null=True)

    # Body
    body = models.TextField(blank=True, null=True)

    # Document ID
    doc_id = models.CharField(max_length=255, blank=True, null=True)

    # Name
    name = models.CharField(max_length=255, blank=True, null=True)

    # Image
    image = models.URLField(
        blank=True, null=True
    )  # Use ImageField if you are uploading images

    # User ID (Foreign Key to User model)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    user = models.CharField(max_length=255, blank=True, null=True)

    # def set_tokens(self, tokens_list):
    #     self.tokens = json.dumps(tokens_list)

    # def get_tokens(self):
    #     return json.loads(self.tokens)

    def __str__(self):
        return self.title
