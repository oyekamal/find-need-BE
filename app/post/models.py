from django.db import models
from accountProfile.models import City, Country
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from enum import Enum


class PostExampleImage(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="post_example", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ImageGroupName(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ImageGroup(models.Model):
    group_name = models.ForeignKey(
        ImageGroupName, on_delete=models.CASCADE, related_name="image_groups"
    )
    image = models.ForeignKey(
        PostExampleImage, on_delete=models.CASCADE, related_name="images_in_group"
    )
    index = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.group_name.name


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


class Extra(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="extra", blank=True, null=True)
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


class RegionSpecs(models.Model):
    image = models.ImageField(upload_to="region_specs", blank=True, null=True)
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PreCategory(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="pre_category", blank=True, null=True)
    name = models.CharField(max_length=100)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="category", blank=True, null=True)
    name = models.CharField(max_length=100)
    pre_category = models.ForeignKey(
        PreCategory,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="categories",
    )
    group_name = models.ForeignKey(
        ImageGroupName,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="categories_in_group",
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


class Warranty(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="color", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to="category", blank=True, null=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostType(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
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
    description = models.TextField(null=True, blank=True)
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
            .filter(delete=False)  # Filter out posts where delete=True
            .order_by("-boost_score")
        )


class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )  # Adding user field
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True, blank=True
    )
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
    region_specs = models.ForeignKey(
        RegionSpecs, on_delete=models.CASCADE, null=True, blank=True
    )
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
    # kilometers = models.PositiveIntegerField(null=True, blank=True)
    kilometers = models.CharField(max_length=200, null=True, blank=True)
    options = models.ManyToManyField("Option", blank=True, null=True)
    extra = models.ManyToManyField(Extra, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True)
    warranty = models.ForeignKey(
        Warranty, on_delete=models.CASCADE, null=True, blank=True
    )
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
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
    # Number of doors
    doors = models.PositiveIntegerField(default=0, null=True, blank=True)
    # Number of cylinders
    cylinders = models.PositiveIntegerField(default=0, null=True, blank=True)
    # Add fields for latitude and longitude
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    loaction_name = models.CharField(max_length=200, null=True, blank=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)
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
        if self.title:
            return self.title
        return ""

    class Meta:
        ordering = ["-created_at"]  # Order by created_at in ascending order
        indexes = [
            models.Index(fields=["user"], name="post_user_idx"),
            models.Index(fields=["city"], name="post_city_idx"),
            models.Index(fields=["category"], name="post_category_idx"),
            models.Index(fields=["sub_category"], name="post_sub_category_idx"),
            models.Index(fields=["post_type"], name="post_post_type_idx"),
            models.Index(fields=["year"], name="post_year_idx"),
            models.Index(fields=["region"], name="post_region_idx"),
            models.Index(fields=["region_specs"], name="post_region_specs_idx"),
            models.Index(fields=["body_condition"], name="post_body_condition_idx"),
            models.Index(
                fields=["mechanical_condition"], name="post_mechanical_condition_idx"
            ),
            models.Index(fields=["transmission"], name="post_transmission_idx"),
            models.Index(fields=["fuel_type"], name="post_fuel_type_idx"),
            models.Index(fields=["insurance"], name="post_insurance_idx"),
            models.Index(fields=["payment_method"], name="post_payment_method_idx"),
            models.Index(fields=["color"], name="post_color_idx"),
            models.Index(fields=["warranty"], name="post_warranty_idx"),
            models.Index(fields=["boost_score"], name="post_boost_score_idx"),
            models.Index(fields=["view_count"], name="post_view_count_idx"),
            models.Index(fields=["doors"], name="post_doors_idx"),
            models.Index(fields=["cylinders"], name="post_cylinders_idx"),
            models.Index(fields=["latitude", "longitude"], name="post_location_idx"),
            models.Index(fields=["created_at"], name="post_created_at_idx"),
            models.Index(fields=["updated_at"], name="post_updated_at_idx"),
        ]


class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "user",
            "post",
        )  # Ensure only one favourite per user/post combo
        ordering = ["-created_at"]  # Order by created_at in ascending order


class ReportStatus(Enum):
    PENDING = "pending"  # Default state
    BLOCKED = "blocked"
    RESOLVED = "resolved"


class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reports")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.name) for status in ReportStatus],
        default=ReportStatus.PENDING.value,
    )

    class Meta:
        ordering = ["-created_at"]  # Order by created_at in ascending order

    def __str__(self):
        return f"Report #{self.id} - {self.post} ({self.status})"


class ReportChat(models.Model):
    REPORT = "report"
    SUPPORT = "support"

    CHAT_TYPE_CHOICES = [
        (REPORT, "Report"),
        (SUPPORT, "Support"),
    ]

    chat_type = models.CharField(
        max_length=10,
        choices=CHAT_TYPE_CHOICES,
        default=REPORT,
    )
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name="report_chats",
        blank=True,
        null=True,
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to="report_chat", blank=True, null=True)
    audio = models.FileField(
        upload_to="report_chat/audio", blank=True, null=True
    )  # Audio file field
    is_admin = models.BooleanField(
        default=False
    )  # Indicates whether the message is from an admin
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]  # Order by created_at in ascending order

    def __str__(self):
        return f"Chat #{self.id} - {self.report}"


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="post", blank=True, null=True)
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BoostRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    boost_package = models.ForeignKey(
        BoostPackage, on_delete=models.SET_NULL, null=True, blank=True
    )
    message = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("PENDING", "Pending"),
            ("APPROVED", "Approved"),
            ("REJECTED", "Rejected"),
        ],
        default="PENDING",
    )
    # ... other fields as needed
    # Add created_at and updated_at fields
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # Order by created_at in ascending order
