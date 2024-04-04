from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
import random

from post.models import (
    Image,
    Condition,
    Transmission,
    FuelType,
    Insurance,
    PaymentMethod,
    Option,
    Extra,
    Region,
    RegionSpecs,
    PreCategory,
    Category,
    Color,
    Warranty,
    Subcategory,
    PostType,
    BoostPackage,
    Post,
    Favourite,
    Report,
    ReportStatus,
    ReportChat,
)

# Faker instance for generating random data
faker = Faker()


class Command(BaseCommand):
    help = "Generate dummy data for posts"

    def handle(self, *args, **options):
        # Create at least 100 posts
        for _ in range(100):
            # Generate random data for post fields
            user = None  # Assuming user object is created elsewhere
            city = None  # Assuming city object is created elsewhere
            pre_category = random.choice(PreCategory.objects.all())
            category = random.choice(pre_category.category_set.all())
            # Create random image instances
            # images = [Image(image=faker.image()) for _ in range(random.randint(1, 3))]
            year = random.randint(2000, 2023)
            region = random.choice(Region.objects.all())
            # region_specs = random.choice(region.regionspecs_set.all())
            body_condition = random.choice(Condition.objects.all())
            mechanical_condition = random.choice(Condition.objects.all())
            transmission = random.choice(Transmission.objects.all())
            fuel_type = random.choice(FuelType.objects.all())
            insurance = random.choice(Insurance.objects.all())
            payment_method = random.choice(PaymentMethod.objects.all())
            kilometers = faker.random_int(min=1000, max=200000)
            # options = random.sample(Option.objects.all(), random.randint(1, 5))
            # extra = random.sample(Extra.objects.all(), random.randint(1, 3))
            color = random.choice(Color.objects.all())
            # warranty = random.choice(Warranty.objects.all())
            title = faker.sentence()
            description = faker.paragraph()
            price = round(random.uniform(10000, 50000), 2)
            phone_number = faker.phone_number()
            # boost_package = random.choice(BoostPackage.objects.all()) if BoostPackage.objects.exists() else None
            view_count = random.randint(10, 1000)
            doors = random.randint(2, 5)
            cylinders = random.randint(3, 8)
            latitude = faker.latitude()
            longitude = faker.longitude()
            # location_name = faker.address()

            # Create the post object
            post = Post.objects.create(
                user=user,
                city=city,
                pre_category=pre_category,
                category=category,
                # images=images,
                year=year,
                region=region,
                # region_specs=region_specs,
                body_condition=body_condition,
                mechanical_condition=mechanical_condition,
                transmission=transmission,
                fuel_type=fuel_type,
                insurance=insurance,
                payment_method=payment_method,
                kilometers=kilometers,
                # options=options,
                # extra=extra,
                color=color,
                # warranty=warranty,
                title=title,
                description=description,
                price=price,
                phone_number=phone_number,
                # boost_package=boost_package,
                view_count=view_count,
                doors=doors,
                cylinders=cylinders,
                latitude=latitude,
                longitude=longitude,
                # location_name=location_name,
            )

            if random.random() < 0.1:  # 10% chance of creating a favorite
                if user:  # Only create favorite if user exists
                    Favourite.objects.create(user=user, post=post)

            # if random.random() < 0.05:  # 5% chance of creating a report
            #     report = Report.objects.create(
            #         post=post, user=random.choice(user.objects.all()), reason=faker.text()
            #     )
            #     # Create 1-2 report chat messages
            #     for _ in range(random.randint(1, 2)):
            #         is_admin = random.random() < 0.5  # 50% chance of admin message
            #         message = faker.text()
            #         image = None
            #         if random.random() < 0.2:  # 20% chance of image attachment
            #             image = faker.image()
            #         audio = None
            #         if random.random() < 0.1:  # 10% chance of audio attachment
            #             audio = faker.binary()  # Simulate audio data
            #         ReportChat.objects.create(
            #             report=report,
            #             user=user if not is_admin else None,  # Only user for non-admin
            #             message=message,
            #             image=image,
            #             audio=audio,
            #             is_admin=is_admin,
            #         )

        self.stdout.write(self.style.SUCCESS(f"Successfully generated 100 dummy posts"))
