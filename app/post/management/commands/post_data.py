import random
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from datetime import timedelta
from accountProfile.models import City, Country
from post.models import (
    PostExampleImage, ImageGroupName, ImageGroup, Image, Condition,
    Transmission, FuelType, Insurance, PaymentMethod, Option, Extra,
    Region, RegionSpecs, PreCategory, Category, Color, Warranty,
    Subcategory, PostType, BoostPackage, Post, Favourite, Report,
    ReportChat, BoostRequest
)

class Command(BaseCommand):
    help = 'Populates the database with detailed sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting database population...')

        # Get or create the User model
        User = get_user_model()

        # Create Users
        users = []
        user_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'password': 'password123'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'password': 'password123'},
            {'username': 'bob_wilson', 'email': 'bob@example.com', 'password': 'password123'},
            {'username': 'alice_brown', 'email': 'alice@example.com', 'password': 'password123'},
            {'username': 'admin_user', 'email': 'admin@example.com', 'password': 'password123'},
        ]
        for data in user_data:
            user, created = User.objects.get_or_create(
                username=data['username'],
                email=data['email'],
                defaults={'password': data['password']}
            )
            if created:
                user.set_password(data['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created User: {data["username"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped User: {data["username"]}'))
            users.append(user)

        # Create Countries
        countries = []
        country_data = [
            {'name': 'United States'},
            {'name': 'Canada'},
            {'name': 'United Kingdom'},
        ]
        for data in country_data:
            country, created = Country.objects.get_or_create(name=data['name'])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Country: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Country: {data["name"]}'))
            countries.append(country)

        # Create Cities
        cities = []
        city_data = [
            {'name': 'New York', 'country': countries[0]},
            {'name': 'Los Angeles', 'country': countries[0]},
            {'name': 'Toronto', 'country': countries[1]},
            {'name': 'London', 'country': countries[2]},
        ]
        for data in city_data:
            city, created = City.objects.get_or_create(
                name=data['name'], country=data['country']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created City: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped City: {data["name"]}'))
            cities.append(city)

        # Create Conditions
        conditions = []
        condition_data = [
            {'name': 'Poor'},
            {'name': 'Fair'},
            {'name': 'Good'},
            {'name': 'Excellent'},
        ]
        for data in condition_data:
            condition, created = Condition.objects.get_or_create(
                name=data['name']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Condition: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Condition: {data["name"]}'))
            conditions.append(condition)

        # Create Transmissions
        transmissions = []
        transmission_data = [
            {'name': 'Automatic'},
            {'name': 'Manual'},
            {'name': 'CVT'},
        ]
        for data in transmission_data:
            transmission, created = Transmission.objects.get_or_create(
                name=data['name']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Transmission: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Transmission: {data["name"]}'))
            transmissions.append(transmission)

        # Create Fuel Types
        fuel_types = []
        fuel_type_data = [
            {'name': 'Gasoline'},
            {'name': 'Diesel'},
            {'name': 'Hybrid'},
            {'name': 'Electric'},
            {'name': 'Plug-in Hybrid'},
        ]
        for data in fuel_type_data:
            fuel_type, created = FuelType.objects.get_or_create(
                name=data['name']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created FuelType: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped FuelType: {data["name"]}'))
            fuel_types.append(fuel_type)

        # Create Insurance Types
        insurances = []
        insurance_data = [
            {'name': 'Compulsory'},
            {'name': 'Comprehensive'},
            {'name': 'Not Insured'},
        ]
        for data in insurance_data:
            insurance, created = Insurance.objects.get_or_create(
                name=data['name']
            )
            insurances.append(insurance)  # Make sure to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Insurance: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Insurance: {data["name"]}'))

        # Debug output for insurances
        self.stdout.write(self.style.SUCCESS(f'Total insurances created: {len(insurances)}'))
        for i, insurance in enumerate(insurances):
            self.stdout.write(self.style.SUCCESS(f'Insurance {i}: {insurance.name}'))

        # Verify insurances were created
        if len(insurances) < 2:
            raise ValueError(f"Not enough insurances were created. Expected at least 2, but got {len(insurances)}")

        # Create Payment Methods
        payment_methods = []
        payment_method_data = [
            {'name': 'Cash'},
            {'name': 'Installments'},
            {'name': 'Cash + Installments'},
        ]
        for data in payment_method_data:
            payment_method, created = PaymentMethod.objects.get_or_create(
                name=data['name']
            )
            payment_methods.append(payment_method)  # Make sure to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created PaymentMethod: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped PaymentMethod: {data["name"]}'))

        # Debug output for payment methods
        self.stdout.write(self.style.SUCCESS(f'Total payment methods created: {len(payment_methods)}'))
        for i, method in enumerate(payment_methods):
            self.stdout.write(self.style.SUCCESS(f'PaymentMethod {i}: {method.name}'))

        # Create Options
        options = []
        option_data = [
            {'name': 'Sunroof'},
            {'name': 'Navigation System'},
            {'name': 'Leather Seats'},
            {'name': 'Cruise Control'},
            {'name': 'Keyless Entry'},
            {'name': 'Backup Camera'},
        ]
        for data in option_data:
            option, created = Option.objects.get_or_create(
                name=data['name']
            )
            options.append(option)  # Make sure to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Option: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Option: {data["name"]}'))

        # Create Extras
        extras = []
        extra_data = [
            {'name': 'Premium Sound System'},
            {'name': 'Parking Sensors'},
            {'name': 'Heated Seats'},
            {'name': 'Third Row Seating'},
        ]
        for data in extra_data:
            extra, created = Extra.objects.get_or_create(
                name=data['name']
            )
            extras.append(extra)  # Make sure to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Extra: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Extra: {data["name"]}'))

        # Create Regions
        regions = []
        region_data = [
            {'name': 'Japanese'},
            {'name': 'American'},
            {'name': 'European'},
            {'name': 'Other'},
        ]
        for data in region_data:
            # Use get_or_create and unpack the tuple properly
            region, created = Region.objects.get_or_create(
                name=data['name']
            )
            regions.append(region)  # Always append regardless of created status
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Region: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Region: {data["name"]}'))

        # Verify regions were created
        self.stdout.write(self.style.SUCCESS(f'Total regions created: {len(regions)}'))
        
        # Debug output
        for i, region in enumerate(regions):
            self.stdout.write(self.style.SUCCESS(f'Region {i}: {region.name}'))

        # Ensure we have enough regions before proceeding
        if len(regions) < 2:
            raise ValueError("Not enough regions were created. Expected at least 2 regions.")

        # Create Region Specs
        region_specs = []
        region_specs_data = [
            {'name': 'GCC Specs'},
            {'name': 'European Specs'},
            {'name': 'American Specs'},
            {'name': 'Japanese Specs'},
        ]
        for data in region_specs_data:
            region_spec, created = RegionSpecs.objects.get_or_create(
                name=data['name']
            )
            region_specs.append(region_spec)  # Add this line to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created RegionSpecs: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped RegionSpecs: {data["name"]}'))

        # Verify region_specs were created
        self.stdout.write(self.style.SUCCESS(f'Total region specs created: {len(region_specs)}'))
        
        # Debug output
        for i, spec in enumerate(region_specs):
            self.stdout.write(self.style.SUCCESS(f'RegionSpec {i}: {spec.name}'))

        # Ensure we have enough region_specs before proceeding
        if len(region_specs) < 1:
            raise ValueError("No region specs were created. Expected at least 1 region spec.")

        # Create Colors
        colors = []
        color_data = [
            {'name': 'Red'},
            {'name': 'Blue'},
            {'name': 'Green'},
            {'name': 'Black'},
            {'name': 'White'},
            {'name': 'Silver'},
        ]
        for data in color_data:
            color, created = Color.objects.get_or_create(
                name=data['name']
            )
            colors.append(color)  # Make sure to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Color: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Color: {data["name"]}'))

        # Create Warranties
        warranties = []
        warranty_data = [
            {'name': '1 Year'},
            {'name': '3 Years'},
            {'name': '5 Years'},
        ]
        for data in warranty_data:
            warranty, created = Warranty.objects.get_or_create(
                name=data['name']
            )
            warranties.append(warranty)  # Make sure to append to the list
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Warranty: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Warranty: {data["name"]}'))

        # Debug output for all created objects
        for list_name, items in [
            ('Payment Methods', payment_methods),
            ('Options', options),
            ('Extras', extras),
            ('Colors', colors),
            ('Warranties', warranties),
        ]:
            self.stdout.write(self.style.SUCCESS(f'\nTotal {list_name} created: {len(items)}'))
            for i, item in enumerate(items):
                self.stdout.write(self.style.SUCCESS(f'{list_name} {i}: {item.name}'))

        # Create PreCategories
        pre_categories = []
        pre_category_data = [
            {'name': 'Vehicles', 'title': 'All Vehicles'},
            {'name': 'Electronics', 'title': 'All Electronics'},
            {'name': 'Accessories', 'title': 'All Accessories'},
        ]
        for data in pre_category_data:
            pre_category, created = PreCategory.objects.get_or_create(
                name=data['name'],
                defaults={'title': data['title']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created PreCategory: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped PreCategory: {data["name"]}'))
            pre_categories.append(pre_category)

        # Create Image Group Names
        image_group_names = []
        image_group_name_data = [
            {'name': 'Vehicle Images', 'description': 'Images for vehicles'},
            {'name': 'Electronics Images', 'description': 'Images for electronics'},
            {'name': 'Accessory Images', 'description': 'Images for accessories'},
        ]
        for data in image_group_name_data:
            image_group_name, created = ImageGroupName.objects.get_or_create(
                name=data['name'], defaults={'description': data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created ImageGroupName: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped ImageGroupName: {data["name"]}'))
            image_group_names.append(image_group_name)

        # Create Categories
        categories = []
        category_data = [
            {
                'name': 'Used Cars',
                'title': 'Used Automobiles',
                'pre_category': pre_categories[0],
                'group_name': image_group_names[0]
            },
            {
                'name': 'Motorcycles',
                'title': 'Motorcycles',
                'pre_category': pre_categories[0],
                'group_name': image_group_names[0]
            },
            {
                'name': 'Auto Accessories',
                'title': 'Car Accessories',
                'pre_category': pre_categories[2],
                'group_name': image_group_names[2]
            },
            {
                'name': 'Smartphones',
                'title': 'Mobile Phones',
                'pre_category': pre_categories[1],
                'group_name': image_group_names[1]
            },
        ]
        for data in category_data:
            category, created = Category.objects.get_or_create(
                name=data['name'],
                defaults={
                    'title': data['title'],
                    'pre_category': data['pre_category'],
                    'group_name': data['group_name']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Category: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Category: {data["name"]}'))
            categories.append(category)

        # Create Subcategories
        subcategories = []
        subcategory_data = [
            {'name': 'Sedans', 'category': categories[0]},
            {'name': 'SUVs', 'category': categories[0]},
            {'name': 'Sport Bike', 'category': categories[1]},
            {'name': 'Adventure/Touring', 'category': categories[1]},
            {'name': 'Car Audio', 'category': categories[2]},
            {'name': 'Android Phones', 'category': categories[3]},
        ]
        for data in subcategory_data:
            subcategory, created = Subcategory.objects.get_or_create(
                name=data['name'],
                category=data['category']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Subcategory: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Subcategory: {data["name"]}'))
            subcategories.append(subcategory)

        # Create Post Types
        post_types = []
        post_type_data = [
            {'name': 'Toyota Camry', 'sub_category': subcategories[0]},
            {'name': 'Honda CR-V', 'sub_category': subcategories[1]},
            {'name': 'Yamaha YZF-R1', 'sub_category': subcategories[2]},
            {'name': 'BMW GS', 'sub_category': subcategories[3]},
            {'name': 'Pioneer Audio', 'sub_category': subcategories[4]},
            {'name': 'Samsung Galaxy', 'sub_category': subcategories[5]},
        ]
        for data in post_type_data:
            post_type, created = PostType.objects.get_or_create(
                name=data['name'],
                sub_category=data['sub_category']
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created PostType: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped PostType: {data["name"]}'))
            post_types.append(post_type)

        # Create Boost Packages
        boost_packages = []
        boost_package_data = [
            {
                'name': 'Basic Boost',
                'description': '7-day visibility boost',
                'duration_days': 7,
                'price': Decimal('9.99')
            },
            {
                'name': 'Premium Boost',
                'description': '30-day premium visibility boost',
                'duration_days': 30,
                'price': Decimal('29.99')
            },
            {
                'name': 'Elite Boost',
                'description': '60-day elite visibility boost',
                'duration_days': 60,
                'price': Decimal('49.99')
            },
        ]
        for data in boost_package_data:
            boost_package, created = BoostPackage.objects.get_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'duration_days': data['duration_days'],
                    'price': data['price']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created BoostPackage: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped BoostPackage: {data["name"]}'))
            boost_packages.append(boost_package)

        # Create Post Example Images
        post_example_images = []
        post_example_image_data = [
            {'name': 'Car Front View', 'description': 'Front view of a car'},
            {'name': 'Car Interior', 'description': 'Interior view of a car'},
            {'name': 'Motorcycle Side', 'description': 'Side view of a motorcycle'},
            {'name': 'Smartphone Display', 'description': 'Smartphone screen display'},
        ]
        for data in post_example_image_data:
            post_example_image, created = PostExampleImage.objects.get_or_create(
                name=data['name'],
                defaults={'description': data['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created PostExampleImage: {data["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped PostExampleImage: {data["name"]}'))
            post_example_images.append(post_example_image)

        # Create Image Groups
        image_groups = []
        image_group_data = [
            {'group_name': image_group_names[0], 'image': post_example_images[0], 'index': 1},
            {'group_name': image_group_names[0], 'image': post_example_images[1], 'index': 2},
            {'group_name': image_group_names[1], 'image': post_example_images[3], 'index': 1},
        ]
        for data in image_group_data:
            image_group, created = ImageGroup.objects.get_or_create(
                group_name=data['group_name'],
                image=data['image'],
                defaults={'index': data['index']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created ImageGroup: {data["group_name"].name} - {data["image"].name}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped ImageGroup: {data["group_name"].name} - {data["image"].name}'))
            image_groups.append(image_group)

        # Before creating posts, validate all required lists have sufficient items
        validation_checks = [
            (users, 3, "users"),
            (cities, 3, "cities"),
            (countries, 2, "countries"),
            (pre_categories, 3, "pre_categories"),
            (categories, 4, "categories"),
            (subcategories, 6, "subcategories"),
            (post_types, 6, "post_types"),
            (regions, 2, "regions"),
            (region_specs, 3, "region_specs"),
            (conditions, 4, "conditions"),
            (transmissions, 2, "transmissions"),
            (fuel_types, 3, "fuel_types"),
            (insurances, 2, "insurances"),
            (payment_methods, 2, "payment_methods"),
            (colors, 6, "colors"),
            (warranties, 2, "warranties"),
            (boost_packages, 3, "boost_packages"),
            (options, 6, "options"),
            (extras, 3, "extras")
        ]

        # Validate all lists have required items
        for item_list, required_length, list_name in validation_checks:
            if len(item_list) < required_length:
                raise ValueError(f"Not enough {list_name} were created. Expected at least {required_length}, but got {len(item_list)}")
            self.stdout.write(self.style.SUCCESS(f'Validated {list_name}: {len(item_list)} items'))

        # Debug output for all lists
        debug_lists = {
            'Users': users,
            'Cities': cities,
            'Countries': countries,
            'PreCategories': pre_categories,
            'Categories': categories,
            'Subcategories': subcategories,
            'PostTypes': post_types,
            'Regions': regions,
            'RegionSpecs': region_specs,
            'Conditions': conditions,
            'Transmissions': transmissions,
            'FuelTypes': fuel_types,
            'Insurances': insurances,
            'PaymentMethods': payment_methods,
            'Colors': colors,
            'Warranties': warranties,
            'BoostPackages': boost_packages,
            'Options': options,
            'Extras': extras
        }

        for list_name, items in debug_lists.items():
            self.stdout.write(self.style.SUCCESS(f'\n{list_name} contents:'))
            for i, item in enumerate(items):
                self.stdout.write(self.style.SUCCESS(f'  {i}: {item}'))

        # Now proceed with post creation only if all validations pass
        posts = []
        post_data = [
            {
                'user': users[0],
                'city': cities[0],
                'country': countries[0],
                'pre_category': pre_categories[0],
                'category': categories[0],
                'sub_category': subcategories[0],
                'post_type': post_types[0],
                'year': 2020,
                'region': regions[1],
                'region_specs': region_specs[0],
                'body_condition': conditions[3],
                'mechanical_condition': conditions[3],
                'transmission': transmissions[0],
                'fuel_type': fuel_types[0],
                'insurance': insurances[1],
                'payment_method': payment_methods[0],
                'kilometers': '25000',
                'color': colors[0],
                'warranty': warranties[1],
                'title': '2020 Toyota Camry SE',
                'description': 'Well-maintained 2020 Toyota Camry SE with low mileage',
                'price': Decimal('25000.00'),
                'phone_number': '+12025550123',
                'boost_package': boost_packages[0],
                'boost_score': 50,
                'view_count': 100,
                'cylinders': 4,
                'latitude': 34.0522,
                'longitude': -118.2437,
                'location_name': 'Los Angeles, CA',
                'sold': False,
                'delete': False,
                'options': [],
                'extras': [extras[0]],
            },
            {
                'user': users[1],
                'city': cities[1],
                'country': countries[0],
                'pre_category': pre_categories[0],
                'category': categories[0],
                'sub_category': subcategories[1],
                'post_type': post_types[1],
                'year': 2019,
                'region': regions[1],
                'region_specs': region_specs[0],
                'body_condition': conditions[2],
                'mechanical_condition': conditions[2],
                'transmission': transmissions[0],
                'fuel_type': fuel_types[2],
                'insurance': insurances[1],
                'payment_method': payment_methods[1],
                'kilometers': '35000',
                'color': colors[1],
                'warranty': warranties[0],
                'title': '2019 Honda CR-V EX-L',
                'description': 'Reliable 2019 Honda CR-V EX-L with hybrid engine',
                'price': Decimal('30000.00'),
                'phone_number': '+13105550123',
                'boost_package': boost_packages[1],
                'boost_score': 75,
                'view_count': 200,
                'cylinders': 4,
                'latitude': 34.0522,
                'longitude': -118.2437,
                'location_name': 'Los Angeles, CA',
                'sold': False,
                'delete': False,
                'options': [options[2], options[4], options[5]],
                'extras': [extras[2]],
            },
            {
                'user': users[2],
                'city': cities[2],
                'country': countries[1],
                'pre_category': pre_categories[0],
                'category': categories[1],
                'sub_category': subcategories[2],
                'post_type': post_types[2],
                'year': 2021,
                'region': regions[0],
                'region_specs': region_specs[2],
                'body_condition': conditions[3],
                'mechanical_condition': conditions[3],
                'transmission': transmissions[1],
                'fuel_type': fuel_types[0],
                'insurance': insurances[0],
                'payment_method': payment_methods[0],
                'kilometers': '10000',
                'color': colors[3],
                'warranty': warranties[1],
                'title': '2021 Yamaha YZF-R1',
                'description': 'Like-new 2021 Yamaha YZF-R1 sport bike',
                'price': Decimal('18000.00'),
                'phone_number': '+14165550123',
                'boost_package': boost_packages[2],
                'boost_score': 90,
                'view_count': 150,
                'cylinders': 0,
                'latitude': 43.6532,
                'longitude': -79.3832,
                'location_name': 'Toronto, ON',
                'sold': False,
                'delete': False,
                'options': [],
                'extras': [extras[0]],
            },
        ]
        for data in post_data:
            try:
                post, created = Post.objects.get_or_create(
                    title=data['title'],
                    user=data['user'],
                    defaults={
                        'city': data['city'],
                        'country': data['country'],
                        'pre_category': data['pre_category'],
                        'category': data['category'],
                        'sub_category': data['sub_category'],
                        'post_type': data['post_type'],
                        'year': data['year'],
                        'region': data['region'],
                        'region_specs': data['region_specs'],
                        'body_condition': data['body_condition'],
                        'mechanical_condition': data['mechanical_condition'],
                        'transmission': data['transmission'],
                        'fuel_type': data['fuel_type'],
                        'insurance': data['insurance'],
                        'payment_method': data['payment_method'],
                        'kilometers': data['kilometers'],
                        'color': data['color'],
                        'warranty': data['warranty'],
                        'description': data['description'],
                        'price': data['price'],
                        'phone_number': data['phone_number'],
                        'boost_package': data['boost_package'],
                        'boost_score': data['boost_score'],
                        'view_count': data['view_count'],
                        'cylinders': data['cylinders'],
                        'latitude': data['latitude'],
                        'longitude': data['longitude'],
                        'location_name': data['location_name'],
                        'sold': data['sold'],
                        'delete': data['delete'],
                    }
                )
                if created:
                    # Add many-to-many relationships after creation
                    post.options.set(data['options'])
                    post.extras.set(data['extras'])
                    self.stdout.write(self.style.SUCCESS(f'Created Post: {data["title"]}'))
                else:
                    self.stdout.write(self.style.NOTICE(f'Skipped Post: {data["title"]}'))
                posts.append(post)
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error creating post {data["title"]}: {str(e)}'))

        # Verify posts were created before proceeding
        if len(posts) == 0:
            raise ValueError("No posts were created successfully. Cannot proceed with creating favorites.")

        # Debug output for posts
        self.stdout.write(self.style.SUCCESS(f'\nTotal posts created: {len(posts)}'))
        for i, post in enumerate(posts):
            self.stdout.write(self.style.SUCCESS(f'Post {i}: {post.title}'))

        # Only create favorites if we have enough posts
        if len(posts) >= 3:
            # Create Favourites
            favourite_data = [
                {'user': users[1], 'post': posts[0]},
                {'user': users[2], 'post': posts[1]},
                {'user': users[3], 'post': posts[2]},
            ]
            for data in favourite_data:
                favourite, created = Favourite.objects.get_or_create(
                    user=data['user'],
                    post=data['post']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created Favourite: User {data["user"].username} - Post {data["post"].title}'))
                else:
                    self.stdout.write(self.style.NOTICE(f'Skipped Favourite: User {data["user"].username} - Post {data["post"].title}'))
        else:
            self.stdout.write(self.style.WARNING('Not enough posts created to create favorites. Skipping favorite creation.'))

        # Create Reports
        reports = []
        report_data = [
            {
                'post': posts[0],
                'user': users[1],
                'reason': 'Inappropriate content in description',
                'status': 'pending'
            },
            {
                'post': posts[1],
                'user': users[2],
                'reason': 'Suspected fake listing',
                'status': 'pending'
            },
        ]
        for data in report_data:
            report, created = Report.objects.get_or_create(
                post=data['post'],
                user=data['user'],
                defaults={'reason': data['reason'], 'status': data['status']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Report: Post {data["post"].title}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped Report: Post {data["post"].title}'))
            reports.append(report)

        # Create Report Chats
        report_chat_data = [
            {
                'report': reports[0],
                'user': users[1],
                'message': 'Please review this listing for inappropriate content',
                'chat_type': 'report',
                'is_admin': False
            },
            {
                'report': reports[0],
                'user': users[4],
                'message': 'We are reviewing your report, thank you for reporting',
                'chat_type': 'report',
                'is_admin': True
            },
        ]
        for data in report_chat_data:
            report_chat, created = ReportChat.objects.get_or_create(
                report=data['report'],
                user=data['user'],
                message=data['message'],
                defaults={'chat_type': data['chat_type'], 'is_admin': data['is_admin']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created ReportChat: Report #{report.id}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped ReportChat: Report #{report.id}'))

        # Create Boost Requests
        boost_request_data = [
            {
                'user': users[0],
                'post': posts[0],
                'boost_package': boost_packages[1],
                'message': 'Please approve premium boost for my car listing',
                'status': 'PENDING'
            },
            {
                'user': users[1],
                'post': posts[1],
                'boost_package': boost_packages[2],
                'message': 'Requesting elite boost for SUV listing',
                'status': 'APPROVED'
            },
        ]
        for data in boost_request_data:
            boost_request, created = BoostRequest.objects.get_or_create(
                user=data['user'],
                post=data['post'],
                boost_package=data['boost_package'],
                defaults={'message': data['message'], 'status': data['status']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created BoostRequest: Post {data["post"].title}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Skipped BoostRequest: Post {data["post"].title}'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
