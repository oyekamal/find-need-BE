from django.db import models
from accountProfile.models import City
from django.conf import settings



# Model for storing uploaded images
class Image(models.Model):
    image = models.ImageField(upload_to='post', blank=True, null=True)

    def __str__(self):
        return self.image.name 
    
# Model for additional options (e.g., sunroof, electric mirror, etc.)
class Option(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Region(models.Model):
    image = models.ImageField(upload_to='region', blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for vehicle categories
class Category(models.Model):
    image = models.ImageField(
        upload_to='category', blank=True, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Model for vehicle categories
class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for car makers (e.g., Acura, Audi, BMW)
class Subcategory(models.Model):
    image = models.ImageField(
        upload_to='category', blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PostType(models.Model):
    image = models.ImageField(
        upload_to='category', blank=True, null=True)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for vehicle posts
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Adding user field
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField('Image')  # Assuming you have an Image model

    # Other fields
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    post_type = models.ForeignKey(PostType, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    CONDITION_CHOICES = [
        ('poor', 'Poor'),
        ('fair', 'Fair'),
        ('good', 'Good'),
        ('excellent', 'Excellent with No Defects'),
        ('other', 'Other'),
    ]
    body_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    mechanical_condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)
    
    kilometers = models.PositiveIntegerField()
    TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    FUEL_CHOICES = [
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electric', 'Electric'),
        ('plug_in_hybrid', 'Plug-in-Hybrid'),
    ]
    fuel_type = models.CharField(max_length=20, choices=FUEL_CHOICES)
    # Other options (many-to-many relationship with Option model)
    options = models.ManyToManyField('Option')
    INSURANCE_CHOICES = [
        ('compulsory', 'Compulsory Insurance'),
        ('comprehensive', 'Comprehensive Insurance'),
        ('not_insured', 'Not Insured'),
    ]
    insurance = models.CharField(max_length=20, choices=INSURANCE_CHOICES)
    
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash Only'),
        ('installments', 'Installments Only'),
        ('cash_installments', 'Cash or Installments'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.title




