from django.core.management.base import BaseCommand
from post.models import *


class Command(BaseCommand):
    help = "Populate initial data for models"

    def handle(self, *args, **options):
        # Populate Condition model
        conditions_data = ["poor", "fair", "good", "excellent", "other"]
        for condition_name in conditions_data:
            Condition.objects.get_or_create(name=condition_name)
            self.stdout.write(self.style.SUCCESS(f"Added Condition: {condition_name}"))

        # Populate Transmission model
        transmissions_data = ["automatic", "manual"]
        for transmission_name in transmissions_data:
            Transmission.objects.get_or_create(name=transmission_name)
            self.stdout.write(
                self.style.SUCCESS(f"Added Transmission: {transmission_name}")
            )

        # Populate FuelType model
        fuel_types_data = ["gasoline", "diesel", "hybrid", "electric", "plug_in_hybrid"]
        for fuel_type_name in fuel_types_data:
            FuelType.objects.get_or_create(name=fuel_type_name)
            self.stdout.write(self.style.SUCCESS(f"Added FuelType: {fuel_type_name}"))

        # Populate Insurance model
        insurance_data = ["compulsory", "comprehensive", "not_insured"]
        for insurance_name in insurance_data:
            Insurance.objects.get_or_create(name=insurance_name)
            self.stdout.write(self.style.SUCCESS(f"Added Insurance: {insurance_name}"))

        # Populate PaymentMethod model
        payment_methods_data = ["cash", "installments", "cash_installments"]
        for payment_method_name in payment_methods_data:
            PaymentMethod.objects.get_or_create(name=payment_method_name)
            self.stdout.write(
                self.style.SUCCESS(f"Added PaymentMethod: {payment_method_name}")
            )
        # Create or skip Options
        options_data = [
            "Sunroof",
            "Electric Mirror",
            "Navigation System",
            "Cruise Control",
            "Keyless Entry",
        ]
        for option in options_data:
            if not Option.objects.filter(name=option).exists():
                Option.objects.create(name=option)
                self.stdout.write(self.style.SUCCESS(f"Added Option: {option}"))
            else:
                self.stdout.write(self.style.NOTICE(f"Skipped Option: {option}"))

        # Create or skip Regions
        regions_data = ["Japanese", "American", "Other"]
        for region in regions_data:
            if not Region.objects.filter(name=region).exists():
                Region.objects.create(name=region)
                self.stdout.write(self.style.SUCCESS(f"Added Region: {region}"))
            else:
                self.stdout.write(self.style.NOTICE(f"Skipped Region: {region}"))

        # Create or skip Categories
        categories_data = [
            "Used Cars",
            "Motorcycles",
            "Auto Accessories and Parts",
            "Heavy Vehicles",
            "Boats",
        ]
        for category in categories_data:
            if not Category.objects.filter(name=category).exists():
                Category.objects.create(name=category)
                self.stdout.write(self.style.SUCCESS(f"Added Category: {category}"))
            else:
                self.stdout.write(self.style.NOTICE(f"Skipped Category: {category}"))

        # Create or skip Subcategories
        subcategories_data = [
            {"name": "Sport Bike", "category": "Motorcycles"},
            {"name": "Adventure/Touring", "category": "Motorcycles"},
            {"name": "Off Road", "category": "Motorcycles"},
            {"name": "Motorboats", "category": "Boats"},
            {"name": "Sailboats", "category": "Boats"},
            {"name": "Fishing Boat", "category": "Boats"},
            {"name": "Outboard Dayboat", "category": "Boats"},
            {"name": "Private Car", "category": "Used Cars"},
            {"name": "Acura", "category": "Used Cars"},
            {"name": "Audi", "category": "Used Cars"},
            {"name": "BMW", "category": "Used Cars"},
        ]

        for subcategory_data in subcategories_data:
            category_name = subcategory_data["category"]
            category = Category.objects.filter(
                name=category_name
            ).first()  # Use filter() and first() instead of get()

            if category:
                if not Subcategory.objects.filter(
                    name=subcategory_data["name"], category=category
                ).exists():
                    Subcategory.objects.create(
                        name=subcategory_data["name"], category=category
                    )
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Added Subcategory: {subcategory_data["name"]}'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.NOTICE(
                            f'Skipped Subcategory: {subcategory_data["name"]}'
                        )
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(f"Category not found: {category_name}")
                )

        # Create or skip PostTypes
        post_types_data = [
            {"name": "MDX", "subcategories": "Acura"},
            {"name": "RDX", "subcategories": "Acura"},
            {"name": "NSX", "subcategories": "Acura"},
            {"name": "A3", "subcategories": "Audi"},
            {"name": "A4", "subcategories": "Audi"},
            {"name": "A7", "subcategories": "Audi"},
            {"name": "Hyper sports", "subcategories": "Sport Bike"},
            {"name": "Super bike", "subcategories": "Sport Bike"},
            {"name": "Super Sports", "subcategories": "Sport Bike"},
            {"name": "Catamaran", "subcategories": "Sailboats"},
            {"name": "Dingly", "subcategories": "Sailboats"},
        ]

        for item in post_types_data:
            subcategory_name = item["subcategories"]
            subcategory = Subcategory.objects.filter(
                name=subcategory_name
            ).first()  # Use filter() and first() instead of get()

            if subcategory:
                if not PostType.objects.filter(
                    name=item["name"], sub_category=subcategory
                ).exists():
                    PostType.objects.create(name=item["name"], sub_category=subcategory)
                    self.stdout.write(
                        self.style.SUCCESS(f'Added PostType: {item["name"]}')
                    )
                else:
                    self.stdout.write(
                        self.style.NOTICE(f'Skipped PostType: {item["name"]}')
                    )
            else:
                self.stdout.write(
                    self.style.ERROR(f"Subcategory not found: {subcategory_name}")
                )

        # Create or skip Colors
        colors_data = ["Red", "Blue", "Green", "Black", "White"]
        for color in colors_data:
            if not Color.objects.filter(name=color).exists():
                Color.objects.create(name=color)
                self.stdout.write(self.style.SUCCESS(f"Added Color: {color}"))
            else:
                self.stdout.write(self.style.NOTICE(f"Skipped Color: {color}"))
