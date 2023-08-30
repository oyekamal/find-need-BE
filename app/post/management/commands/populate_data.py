from django.core.management.base import BaseCommand
from post.models import Option, Region, Category, CarMaker, CarModel

class Command(BaseCommand):
    help = 'Populate initial data for models'

    def handle(self, *args, **options):
        # Create or skip Options
        options = ['Sunroof', 'Electric Mirror', 'Navigation System', 'Cruise Control', 'Keyless Entry']
        for option in options:
            if not Option.objects.filter(name=option).exists():
                Option.objects.create(name=option)
                self.stdout.write(self.style.SUCCESS(f'Added Option: {option}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Option: {option}'))

        # Create or skip Regions
        regions = ['Japanese', 'American', 'Other']
        for region in regions:
            if not Region.objects.filter(name=region).exists():
                Region.objects.create(name=region)
                self.stdout.write(self.style.SUCCESS(f'Added Region: {region}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Region: {region}'))

        # Create or skip Categories
        categories = ['Used Cars', 'Motorcycles', 'Auto Accessories and Parts', 'Heavy Vehicles']
        for category in categories:
            if not Category.objects.filter(name=category).exists():
                Category.objects.create(name=category)
                self.stdout.write(self.style.SUCCESS(f'Added Category: {category}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Category: {category}'))

        # Create or skip Car Makers
        car_makers = ['Acura', 'Audi', 'BMW']
        for car_maker in car_makers:
            if not CarMaker.objects.filter(name=car_maker).exists():
                CarMaker.objects.create(name=car_maker)
                self.stdout.write(self.style.SUCCESS(f'Added Car Maker: {car_maker}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Car Maker: {car_maker}'))

        # Create or skip Car Models
        car_models = [
            {'maker': 'Acura', 'models': ['MDX', 'RDX', 'NSX']},
            {'maker': 'Audi', 'models': ['A3', 'A4', 'Q7']},
            {'maker': 'BMW', 'models': ['X5', 'M3', 'i8']}
        ]

        for item in car_models:
            try:
                maker = CarMaker.objects.filter(name=item['maker']).first()
            except CarMaker.DoesNotExist:
                continue  # Skip if the CarMaker doesn't exist

            for model in item['models']:
                if not CarModel.objects.filter(maker=maker, name=model).exists():
                    CarModel.objects.create(maker=maker, name=model)
                    self.stdout.write(self.style.SUCCESS(f'Added Car Model: {maker} - {model}'))
                else:
                    self.stdout.write(self.style.NOTICE(f'Skipped Car Model: {maker} - {model}'))

