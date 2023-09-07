from django.core.management.base import BaseCommand
from post.models import Option, Region, Category, Subcategory, PostType, Color, Post
from accountProfile.models import City, CustomUser  # Import the City model from your app
from django.conf import settings
from random import randint, choice  # Import random for generating random data

class Command(BaseCommand):
    help = 'Populate initial data for models'

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
            post = Post(
                user=CustomUser.objects.first(),  # You need to specify the actual user here
                city=choice(cities),
                category=choice(categories),
                sub_category=choice(subcategories),
                post_type=choice(post_types),
                year=randint(2000, 2023),
                region=choice(regions),
                body_condition=choice(['poor', 'fair', 'good', 'excellent', 'other']),
                mechanical_condition=choice(['poor', 'fair', 'good', 'excellent', 'other']),
                kilometers=randint(1, 200000),
                transmission=choice(['automatic', 'manual']),
                fuel_type=choice(['gasoline', 'diesel', 'hybrid', 'electric', 'plug_in_hybrid']),
                insurance=choice(['compulsory', 'comprehensive', 'not_insured']),
                color=choice(colors),
                payment_method=choice(['cash', 'installments', 'cash_installments']),
                title=f'Test Ad {i + 1}',
                description=f'This is a test ad number {i + 1}.',
                price=randint(1000, 50000),
                phone_number='1234567890',
            )
            post.save()
            post.options.set(options.filter(name__in=['Sunroof', 'Navigation System']))  # Add some options
            self.stdout.write(self.style.SUCCESS(f'Added Post: {post.title}'))
