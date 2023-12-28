from django.core.management.base import BaseCommand
from post.models import Option, Region, Category, Subcategory, PostType, Color, Post
from accountProfile.models import (
    City,
    CustomUser,
)  # Import the City model from your app
from django.conf import settings
from random import randint, choice  # Import random for generating random data


class Command(BaseCommand):
    help = "Populate initial data for models"

    def handle(self, *args, **options):
        # Assume you have some initial data for the following models
        cities = City.objects.all()
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        post_types = PostType.objects.all()
        regions = Region.objects.all()
        options = Option.objects.all()
        colors = Color.objects.all()

        # Create or skip Posts
        for i in range(100):  # Adjust the number of posts you want to create
            choice_categories = choice(categories)
            # Check if subcategories for the chosen category exist
            subcategories_for_category = subcategories.filter(
                category=choice_categories
            )
            if subcategories_for_category.exists():
                choice_subcategories = choice(subcategories_for_category)
            else:
                self.stdout.write(
                    self.style.NOTICE(
                        f"Skipped Post: No subcategories for {choice_categories}"
                    )
                )
                continue

            # Check if post types for the chosen subcategory exist
            post_types_for_subcategory = post_types.filter(
                sub_category=choice_subcategories
            )
            if post_types_for_subcategory.exists():
                choice_post_types = choice(post_types_for_subcategory)
            else:
                self.stdout.write(
                    self.style.NOTICE(
                        f"Skipped Post: No post types for {choice_subcategories}"
                    )
                )
                continue
            post = Post(
                user=CustomUser.objects.first(),  # You need to specify the actual user here
                city=choice(cities),
                category=choice_categories,
                sub_category=choice_subcategories,
                post_type=choice_post_types,
                year=randint(2000, 2023),
                region=choice(regions),
                body_condition=choice(["poor", "fair", "good", "excellent", "other"]),
                mechanical_condition=choice(
                    ["poor", "fair", "good", "excellent", "other"]
                ),
                kilometers=randint(1, 200000),
                transmission=choice(["automatic", "manual"]),
                fuel_type=choice(
                    ["gasoline", "diesel", "hybrid", "electric", "plug_in_hybrid"]
                ),
                insurance=choice(["compulsory", "comprehensive", "not_insured"]),
                color=choice(colors),
                payment_method=choice(["cash", "installments", "cash_installments"]),
                title=f"Test Ad {i + 1}",
                description=f"This is a test ad number {i + 1}.",
                price=randint(1000, 50000),
                phone_number="1234567890",
            )
            post.save()
            post.options.set(
                options.filter(name__in=["Sunroof", "Navigation System"])
            )  # Add some options
            self.stdout.write(self.style.SUCCESS(f"Added Post: {post.title}"))
