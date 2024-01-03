from django.db import models
from accountProfile.models import City
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class Image(models.Model):
    image = models.ImageField(upload_to="post", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Condition(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="condition", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="transmission", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="fuel_type", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="insurance", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="payment_method", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="option", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    image = models.ImageField(upload_to="region", blank=True, null=True)
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PreCategory(models.Model):
    image = models.ImageField(upload_to="pre_category", blank=True, null=True)
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    image = models.ImageField(upload_to="category", blank=True, null=True)
    name = models.CharField(max_length=100)
    pre_category = models.ForeignKey(
        PreCategory, on_delete=models.CASCADE, blank=True, null=True
    )
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="color", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    image = models.ImageField(upload_to="category", blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostType(models.Model):
    image = models.ImageField(upload_to="category", blank=True, null=True)
    sub_category = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BoostPackage(models.Model):
    name = models.CharField(max_length=100)
    duration_days = models.PositiveIntegerField()  # Duration of boost in days
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostManager(models.Manager):
    def get_queryset(self):
        # Filter out expired boosted posts and order by boost score
        return (
            super()
            .get_queryset()
            .filter(
                models.Q(boost_package__isnull=True)
                | models.Q(expiration_date__gt=timezone.now())
            )
            .order_by("-boost_score")
        )


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )  # Adding user field
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    pre_category = models.ForeignKey(
        PreCategory, on_delete=models.CASCADE, blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    # Assuming you have an Image model
    # images = models.ManyToManyField("Image", null=True, blank=True)
    # Other fields
    sub_category = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, null=True, blank=True
    )
    post_type = models.ForeignKey(
        PostType, on_delete=models.CASCADE, null=True, blank=True
    )
    year = models.PositiveIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    body_condition = models.ForeignKey(
        Condition, on_delete=models.CASCADE, blank=True, null=True
    )
    mechanical_condition = models.ForeignKey(
        Condition,
        on_delete=models.CASCADE,
        related_name="mechanical_posts",
        blank=True,
        null=True,
    )
    transmission = models.ForeignKey(
        Transmission, on_delete=models.CASCADE, blank=True, null=True
    )
    fuel_type = models.ForeignKey(
        FuelType, on_delete=models.CASCADE, blank=True, null=True
    )
    insurance = models.ForeignKey(
        Insurance, on_delete=models.CASCADE, blank=True, null=True
    )
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE, blank=True, null=True
    )
    kilometers = models.PositiveIntegerField(null=True, blank=True)
    options = models.ManyToManyField("Option")
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    # ForeignKey to represent the selected boost package
    boost_package = models.ForeignKey(
        BoostPackage, on_delete=models.SET_NULL, null=True, blank=True
    )
    # Add a field for the boost score
    boost_score = models.IntegerField(default=0, null=True, blank=True)
    # Add an expiration date field
    expiration_date = models.DateTimeField(null=True, blank=True)
    # Number of times the post has been viewed
    view_count = models.PositiveIntegerField(default=0, null=True, blank=True)
    # Add fields for latitude and longitude
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    loaction_name = models.CharField(max_length=200, null=True, blank=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete = models.BooleanField(default=False)
    # Add the custom manager
    objects = PostManager()

    def save(self, *args, **kwargs):
        # Calculate the expiration date based on the boost package duration
        if self.boost_package:
            self.expiration_date = timezone.now() + timedelta(
                days=self.boost_package.duration_days
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="post", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
