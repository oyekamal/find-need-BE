from django.db import models
from accountProfile.models import City
from django.conf import settings
from django.utils import timezone
from datetime import timedelta

# Model for storing uploaded images
class Image(models.Model):
    image = models.ImageField(upload_to='post', blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.image.name

class Condition(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transmission(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FuelType(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Insurance(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PaymentMethod(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Option(models.Model):
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Region(models.Model):
    image = models.ImageField(upload_to='region', blank=True, null=True)
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Model for vehicle categories


class PreCategory(models.Model):
    image = models.ImageField(
        upload_to='pre_category', blank=True, null=True)
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Category(models.Model):
    image = models.ImageField(
        upload_to='category', blank=True, null=True)
    name = models.CharField(max_length=100)
    pre_category = models.ForeignKey(PreCategory, on_delete=models.CASCADE, blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    image = models.ImageField(
        upload_to='category', blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class PostType(models.Model):
    image = models.ImageField(
        upload_to='category', blank=True, null=True)
    sub_category = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, null=True, blank=True)
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
        return super().get_queryset().filter(
            models.Q(boost_package__isnull=True) | models.Q(expiration_date__gt=timezone.now())
        ).order_by('-boost_score')

# Model for vehicle posts
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)  # Adding user field
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    pre_category = models.ForeignKey(PreCategory, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Assuming you have an Image model
    images = models.ManyToManyField('Image')

    # Other fields
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    post_type = models.ForeignKey(PostType, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    # CONDITION_CHOICES = [
    #     ('poor', 'Poor'),
    #     ('fair', 'Fair'),
    #     ('good', 'Good'),
    #     ('excellent', 'Excellent with No Defects'),
    #     ('other', 'Other'),
    # ]
    # body_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    body_condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True, null=True)
    mechanical_condition = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='mechanical_posts', blank=True, null=True)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, blank=True, null=True)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, blank=True, null=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, blank=True, null=True)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, blank=True, null=True)

    # mechanical_condition = models.CharField(
    #     max_length=20, choices=CONDITION_CHOICES)

    kilometers = models.PositiveIntegerField()
    # TRANSMISSION_CHOICES = [
    #     ('automatic', 'Automatic'),
    #     ('manual', 'Manual'),
    # ]
    # transmission = models.CharField(
    #     max_length=20, choices=TRANSMISSION_CHOICES)
    # FUEL_CHOICES = [
    #     ('gasoline', 'Gasoline'),
    #     ('diesel', 'Diesel'),
    #     ('hybrid', 'Hybrid'),
    #     ('electric', 'Electric'),
    #     ('plug_in_hybrid', 'Plug-in-Hybrid'),
    # ]
    # fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    # Other options (many-to-many relationship with Option model)
    options = models.ManyToManyField('Option')
    # INSURANCE_CHOICES = [
    #     ('compulsory', 'Compulsory Insurance'),
    #     ('comprehensive', 'Comprehensive Insurance'),
    #     ('not_insured', 'Not Insured'),
    # ]
    # insurance = models.CharField(max_length=20, choices=INSURANCE_CHOICES)

    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    # PAYMENT_METHOD_CHOICES = [
    #     ('cash', 'Cash Only'),
    #     ('installments', 'Installments Only'),
    #     ('cash_installments', 'Cash or Installments'),
    # ]
    # payment_method = models.CharField(
    #     max_length=20, choices=PAYMENT_METHOD_CHOICES)

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=50)

    # ForeignKey to represent the selected boost package
    boost_package = models.ForeignKey(BoostPackage, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Add a field for the boost score
    boost_score = models.IntegerField(default=0)
    
    # Add an expiration date field
    expiration_date = models.DateTimeField(null=True, blank=True)
    
    view_count = models.PositiveIntegerField(default=0)  # Number of times the post has been viewed

    # Add fields for latitude and longitude
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    loaction_name = models.CharField(max_length=200, null=True, blank=True)

    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add the custom manager
    objects = PostManager()
    
    def save(self, *args, **kwargs):
        # Calculate the expiration date based on the boost package duration
        if self.boost_package:
            self.expiration_date = timezone.now() + timedelta(days=self.boost_package.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title