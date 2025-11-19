from django.core.management.base import BaseCommand
from post.models import (
    Condition, Transmission, FuelType, Insurance, PaymentMethod, Option, Extra,
    Region, RegionSpecs, PreCategory, Category, Subcategory, PostType, Color,
    Warranty, BoostPackage, Post, Favourite, Report, ReportStatus, ReportChat,
    BoostRequest, PostExampleImage, ImageGroupName, ImageGroup
)
from post.models import Image as PostImage  # Rename to avoid conflict with PIL.Image
from accountProfile.models import (
    Language, Country, City, Follow, Block, ChatMessage, Notification
)
from django.contrib.auth import get_user_model
from decimal import Decimal
import random

User = get_user_model()


class Command(BaseCommand):
    help = "Populate comprehensive dummy data for all models"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("🚀 Starting comprehensive data population..."))
        
        # Create basic data
        languages = self.create_languages()
        countries = self.create_countries()
        cities = self.create_cities(countries)
        users = self.create_users(countries, languages)
        
        # Create relationships
        self.create_relationships(users)
        
        # Create post-related data
        post_data = self.create_post_components()
        
        # Create posts
        posts = self.create_posts(users, cities, post_data)
        
        # Create post interactions
        self.create_post_interactions(users, posts, post_data['boost_packages'])
        
        self.print_summary()

    def create_languages(self):
        self.stdout.write(self.style.SUCCESS("Creating Languages..."))
        languages_data = [
            "English", "Arabic", "Spanish", "French", "German", 
            "Italian", "Portuguese", "Russian", "Chinese", "Japanese"
        ]
        languages = []
        for lang_name in languages_data:
            language, created = Language.objects.get_or_create(name=lang_name)
            languages.append(language)
        return languages

    def create_countries(self):
        self.stdout.write(self.style.SUCCESS("Creating Countries..."))
        countries_data = [
            "United States", "United Kingdom", "Canada", "Australia", "Germany",
            "France", "Spain", "Italy", "Japan", "South Korea", "UAE", "Saudi Arabia"
        ]
        countries = []
        for country_name in countries_data:
            country, created = Country.objects.get_or_create(name=country_name)
            countries.append(country)
        return countries

    def create_cities(self, countries):
        self.stdout.write(self.style.SUCCESS("Creating Cities..."))
        cities_data = [
            {"name": "New York", "country": "United States"},
            {"name": "Los Angeles", "country": "United States"},
            {"name": "London", "country": "United Kingdom"},
            {"name": "Manchester", "country": "United Kingdom"},
            {"name": "Toronto", "country": "Canada"},
            {"name": "Sydney", "country": "Australia"},
            {"name": "Berlin", "country": "Germany"},
            {"name": "Paris", "country": "France"},
            {"name": "Tokyo", "country": "Japan"},
            {"name": "Seoul", "country": "South Korea"},
            {"name": "Dubai", "country": "UAE"},
            {"name": "Riyadh", "country": "Saudi Arabia"},
        ]
        cities = []
        for city_data in cities_data:
            country = Country.objects.filter(name=city_data["country"]).first()
            if country:
                city, created = City.objects.get_or_create(
                    name=city_data["name"], 
                    country=country
                )
                cities.append(city)
        return cities

    def create_users(self, countries, languages):
        self.stdout.write(self.style.SUCCESS("Creating Users..."))
        users_data = [
            {"email": "john.doe@example.com", "username": "johndoe", "first_name": "John", "last_name": "Doe"},
            {"email": "jane.smith@example.com", "username": "janesmith", "first_name": "Jane", "last_name": "Smith"},
            {"email": "mike.johnson@example.com", "username": "mikejohnson", "first_name": "Mike", "last_name": "Johnson"},
            {"email": "sarah.wilson@example.com", "username": "sarahwilson", "first_name": "Sarah", "last_name": "Wilson"},
            {"email": "david.brown@example.com", "username": "davidbrown", "first_name": "David", "last_name": "Brown"},
            {"email": "lisa.garcia@example.com", "username": "lisagarcia", "first_name": "Lisa", "last_name": "Garcia"},
            {"email": "robert.martinez@example.com", "username": "robertmartinez", "first_name": "Robert", "last_name": "Martinez"},
            {"email": "emily.anderson@example.com", "username": "emilyanderson", "first_name": "Emily", "last_name": "Anderson"},
            {"email": "james.taylor@example.com", "username": "jamestaylor", "first_name": "James", "last_name": "Taylor"},
            {"email": "maria.rodriguez@example.com", "username": "mariarodriguez", "first_name": "Maria", "last_name": "Rodriguez"},
        ]
        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                email=user_data["email"],
                defaults={
                    "username": user_data["username"],
                    "first_name": user_data["first_name"],
                    "last_name": user_data["last_name"],
                    "phone_number": f"+123456789{random.randint(0, 9)}",
                    "country": random.choice(countries),
                    "address": f"{random.randint(100, 999)} Main Street",
                    "latitude": str(random.uniform(25.0, 50.0)),
                    "longitude": str(random.uniform(-125.0, -70.0)),
                    "is_online": random.choice([True, False]),
                    "information": f"Bio for {user_data['first_name']} {user_data['last_name']}"
                }
            )
            if created:
                user.set_password("password123")
                user.languages.set(random.sample(languages, random.randint(1, 3)))
                user.save()
            users.append(user)
        return users

    def create_relationships(self, users):
        self.stdout.write(self.style.SUCCESS("Creating Relationships..."))
        
        # Follow relationships
        for _ in range(20):
            follower = random.choice(users)
            following = random.choice(users)
            if follower != following:
                Follow.objects.get_or_create(follower=follower, following=following)

        # Block relationships
        for _ in range(5):
            blocker = random.choice(users)
            blocked = random.choice(users)
            if blocker != blocked:
                Block.objects.get_or_create(blocker=blocker, blocked=blocked)

        # Chat Messages
        messages = [
            "Hello, how are you?", "Is this item still available?", 
            "What's the best price?", "Can we meet tomorrow?",
            "Thanks for the information!", "Great deal!",
        ]
        for _ in range(30):
            sender = random.choice(users)
            receiver = random.choice(users)
            if sender != receiver:
                ChatMessage.objects.create(
                    sender=sender,
                    receiver=receiver,
                    message=random.choice(messages)
                )

    def create_post_components(self):
        self.stdout.write(self.style.SUCCESS("Creating Post Components..."))
        
        # Create conditions
        conditions_data = ["poor", "fair", "good", "excellent", "like new"]
        conditions = [Condition.objects.get_or_create(name=name)[0] for name in conditions_data]
        
        # Create transmissions
        transmissions_data = ["automatic", "manual", "cvt", "dual-clutch"]
        transmissions = [Transmission.objects.get_or_create(name=name)[0] for name in transmissions_data]
        
        # Create fuel types
        fuel_types_data = ["gasoline", "diesel", "hybrid", "electric", "plug_in_hybrid"]
        fuel_types = [FuelType.objects.get_or_create(name=name)[0] for name in fuel_types_data]
        
        # Create insurances
        insurance_data = ["compulsory", "comprehensive", "third_party", "not_insured"]
        insurances = [Insurance.objects.get_or_create(name=name)[0] for name in insurance_data]
        
        # Create payment methods
        payment_methods_data = ["cash", "installments", "cash_installments", "bank_transfer"]
        payment_methods = [PaymentMethod.objects.get_or_create(name=name)[0] for name in payment_methods_data]
        
        # Create options
        options_data = [
            "Sunroof", "Electric Mirror", "Navigation System", "Cruise Control", 
            "Keyless Entry", "Leather Seats", "Heated Seats", "Backup Camera"
        ]
        options = [Option.objects.get_or_create(name=name)[0] for name in options_data]
        
        # Create extras
        extras_data = ["Spare Tire", "Car Cover", "Floor Mats", "Roof Rack", "Winter Tires"]
        extras = [Extra.objects.get_or_create(name=name)[0] for name in extras_data]
        
        # Create regions
        regions_data = ["Japanese", "American", "European", "Korean", "Other"]
        regions = [Region.objects.get_or_create(name=name)[0] for name in regions_data]
        
        # Create region specs
        region_specs_data = ["GCC Specs", "US Specs", "European Specs", "Japanese Specs"]
        region_specs = [RegionSpecs.objects.get_or_create(name=name)[0] for name in region_specs_data]
        
        # Create pre-categories
        pre_categories_data = [
            {"name": "Vehicles", "title": "All Vehicles"},
            {"name": "Marine", "title": "Marine Vehicles"},
        ]
        pre_categories = []
        for pre_cat_data in pre_categories_data:
            pre_cat, created = PreCategory.objects.get_or_create(
                name=pre_cat_data["name"],
                defaults={"title": pre_cat_data["title"]}
            )
            pre_categories.append(pre_cat)
        
        # Create categories
        categories_data = [
            {"name": "Used Cars", "title": "Used Cars for Sale", "pre_category": "Vehicles"},
            {"name": "Motorcycles", "title": "Motorcycles for Sale", "pre_category": "Vehicles"},
            {"name": "Boats", "title": "Boats for Sale", "pre_category": "Marine"},
        ]
        categories = []
        for cat_data in categories_data:
            pre_cat = PreCategory.objects.filter(name=cat_data["pre_category"]).first()
            category, created = Category.objects.get_or_create(
                name=cat_data["name"],
                defaults={"title": cat_data["title"], "pre_category": pre_cat}
            )
            categories.append(category)
        
        # Create subcategories
        subcategories_data = [
            {"name": "Toyota", "category": "Used Cars"},
            {"name": "Honda", "category": "Used Cars"},
            {"name": "BMW", "category": "Used Cars"},
            {"name": "Audi", "category": "Used Cars"},
            {"name": "Sport Bike", "category": "Motorcycles"},
            {"name": "Sailboats", "category": "Boats"},
        ]
        subcategories = []
        for subcat_data in subcategories_data:
            category = Category.objects.filter(name=subcat_data["category"]).first()
            if category:
                subcategory, created = Subcategory.objects.get_or_create(
                    name=subcat_data["name"],
                    category=category
                )
                subcategories.append(subcategory)
        
        # Create post types
        post_types_data = [
            {"name": "Camry", "subcategory": "Toyota"},
            {"name": "Corolla", "subcategory": "Toyota"},
            {"name": "Civic", "subcategory": "Honda"},
            {"name": "Accord", "subcategory": "Honda"},
            {"name": "X3", "subcategory": "BMW"},
            {"name": "3 Series", "subcategory": "BMW"},
            {"name": "A4", "subcategory": "Audi"},
            {"name": "Super Sports", "subcategory": "Sport Bike"},
            {"name": "Catamaran", "subcategory": "Sailboats"},
        ]
        post_types = []
        for pt_data in post_types_data:
            subcategory = Subcategory.objects.filter(name=pt_data["subcategory"]).first()
            if subcategory:
                post_type, created = PostType.objects.get_or_create(
                    name=pt_data["name"],
                    sub_category=subcategory
                )
                post_types.append(post_type)
        
        # Create colors
        colors_data = ["Red", "Blue", "Green", "Black", "White", "Silver", "Gray"]
        colors = [Color.objects.get_or_create(name=name)[0] for name in colors_data]
        
        # Create warranties
        warranties_data = ["No Warranty", "3 Months", "6 Months", "1 Year", "2 Years"]
        warranties = [Warranty.objects.get_or_create(name=name)[0] for name in warranties_data]
        
        # Create boost packages
        boost_packages_data = [
            {"name": "Basic Boost", "description": "3-day boost", "duration": 3, "price": 25.00},
            {"name": "Standard Boost", "description": "7-day boost", "duration": 7, "price": 50.00},
            {"name": "Premium Boost", "description": "14-day boost", "duration": 14, "price": 90.00},
        ]
        boost_packages = []
        for bp_data in boost_packages_data:
            boost_package, created = BoostPackage.objects.get_or_create(
                name=bp_data["name"],
                defaults={
                    "description": bp_data["description"],
                    "duration_days": bp_data["duration"],
                    "price": Decimal(str(bp_data["price"]))
                }
            )
            boost_packages.append(boost_package)

        return {
            'conditions': conditions,
            'transmissions': transmissions,
            'fuel_types': fuel_types,
            'insurances': insurances,
            'payment_methods': payment_methods,
            'options': options,
            'extras': extras,
            'regions': regions,
            'region_specs': region_specs,
            'categories': categories,
            'subcategories': subcategories,
            'post_types': post_types,
            'colors': colors,
            'warranties': warranties,
            'boost_packages': boost_packages,
        }

    def create_posts(self, users, cities, post_data):
        self.stdout.write(self.style.SUCCESS("Creating Posts..."))
        
        car_titles = [
            "Excellent condition Honda Civic", "Well maintained Toyota Camry", 
            "Low mileage BMW 3 Series", "Perfect family car",
            "Sporty Honda Accord", "Reliable Toyota Corolla",
            "Luxury Audi A4 sedan", "Powerful BMW X3 SUV"
        ]
        
        descriptions = [
            "This vehicle has been well maintained and is in excellent condition.",
            "Low mileage vehicle with full service history.",
            "One owner vehicle, garage kept, no accidents.",
            "Great family vehicle with plenty of space.",
            "Fuel efficient and reliable transportation."
        ]

        posts = []
        # Create 50 posts with varied data
        for i in range(50):
            user = random.choice(users)
            city = random.choice(cities)
            
            # Choose category (focus on cars mostly)
            car_categories = [cat for cat in post_data['categories'] if cat.name == "Used Cars"]
            category = random.choice(car_categories) if car_categories else random.choice(post_data['categories'])
            
            # Filter subcategories based on category
            available_subcats = [sc for sc in post_data['subcategories'] if sc.category == category]
            if not available_subcats:
                continue
                
            subcategory = random.choice(available_subcats)
            
            # Filter post types based on subcategory
            available_post_types = [pt for pt in post_data['post_types'] if pt.sub_category == subcategory]
            post_type = random.choice(available_post_types) if available_post_types else None
            
            post = Post.objects.create(
                user=user,
                city=city,
                country=city.country,
                category=category,
                sub_category=subcategory,
                post_type=post_type,
                year=random.randint(2010, 2024),
                region=random.choice(post_data['regions']),
                region_specs=random.choice(post_data['region_specs']),
                body_condition=random.choice(post_data['conditions']),
                mechanical_condition=random.choice(post_data['conditions']),
                transmission=random.choice(post_data['transmissions']),
                fuel_type=random.choice(post_data['fuel_types']),
                insurance=random.choice(post_data['insurances']),
                payment_method=random.choice(post_data['payment_methods']),
                kilometers=f"{random.randint(10, 200)}K",
                color=random.choice(post_data['colors']),
                warranty=random.choice(post_data['warranties']),
                title=random.choice(car_titles),
                description=random.choice(descriptions),
                price=Decimal(str(random.randint(5000, 50000))),
                phone_number=f"+{random.randint(1000000000, 9999999999)}",
                boost_package=random.choice(post_data['boost_packages']) if random.random() < 0.3 else None,
                boost_score=random.randint(0, 100),
                view_count=random.randint(0, 1000),
                doors=random.choice([2, 4, 5]) if category.name == "Used Cars" else None,
                cylinders=random.choice([4, 6, 8]) if category.name == "Used Cars" else None,
                latitude=random.uniform(25.0, 50.0),
                longitude=random.uniform(-125.0, -70.0),
                loaction_name=f"{city.name}, {city.country.name}",
                sold=random.choice([True, False]) if random.random() < 0.1 else False,
            )
            
            # Add random options and extras
            post.options.set(random.sample(post_data['options'], random.randint(2, 4)))
            post.extra.set(random.sample(post_data['extras'], random.randint(1, 3)))
            
            posts.append(post)
            
        self.stdout.write(self.style.SUCCESS(f"Created {len(posts)} posts"))
        return posts

    def create_post_interactions(self, users, posts, boost_packages):
        self.stdout.write(self.style.SUCCESS("Creating Post Interactions..."))
        
        # Create favourites
        for _ in range(100):
            user = random.choice(users)
            post = random.choice(posts)
            Favourite.objects.get_or_create(user=user, post=post)

        # Create reports
        report_reasons = [
            "Inappropriate content", "Spam or fake listing", 
            "Overpriced item", "Misleading description"
        ]
        reports = []
        for _ in range(20):
            user = random.choice(users)
            post = random.choice(posts)
            report = Report.objects.create(
                post=post,
                user=user,
                reason=random.choice(report_reasons),
                status=random.choice([status.value for status in ReportStatus])
            )
            reports.append(report)

        # Create report chats
        chat_messages = [
            "I need help with this issue", "This listing seems suspicious",
            "Can you please investigate this?", "Thank you for your help"
        ]
        for report in reports[:10]:
            for _ in range(random.randint(1, 3)):
                ReportChat.objects.create(
                    report=report,
                    user=report.user,
                    message=random.choice(chat_messages),
                    is_admin=random.choice([True, False])
                )

        # Create post images
        for post in posts[:20]:
            for _ in range(random.randint(1, 4)):
                PostImage.objects.create(post=post)

        # Create boost requests
        for _ in range(15):
            user = random.choice(users)
            post = random.choice(posts)
            boost_package = random.choice(boost_packages)
            BoostRequest.objects.create(
                user=user,
                post=post,
                boost_package=boost_package,
                message=f"Please boost my listing for {post.title}",
                status=random.choice(["PENDING", "APPROVED", "REJECTED"])
            )

        # Create notifications
        notification_titles = [
            "New message received", "Your post has been boosted", 
            "Someone liked your post", "New follower"
        ]
        notification_bodies = [
            "You have received a new message from a user",
            "Your listing is now featured for increased visibility",
            "A user has added your post to favorites",
            "A new user is now following you"
        ]
        
        for _ in range(100):
            user_id = str(random.choice(users).id)
            Notification.objects.create(
                token='["dummy_token_123", "dummy_token_456"]',
                notification_type=random.choice(["info", "warning", "alert", "chat", "post"]),
                title=random.choice(notification_titles),
                body=random.choice(notification_bodies),
                doc_id=str(random.randint(1, 1000)),
                name=f"notification_{random.randint(1, 1000)}",
                image="https://example.com/notification.jpg",
                user=user_id,
                is_read=random.choice([True, False])
            )

    def print_summary(self):
        self.stdout.write(
            self.style.SUCCESS(
                f"\n🎉 Successfully populated database with comprehensive dummy data!\n"
                f"📊 Summary:\n"
                f"   - {Language.objects.count()} Languages\n"
                f"   - {Country.objects.count()} Countries\n"
                f"   - {City.objects.count()} Cities\n"
                f"   - {User.objects.count()} Users\n"
                f"   - {Follow.objects.count()} Follow relationships\n"
                f"   - {ChatMessage.objects.count()} Chat messages\n"
                f"   - {Category.objects.count()} Categories\n"
                f"   - {Subcategory.objects.count()} Subcategories\n"
                f"   - {PostType.objects.count()} Post types\n"
                f"   - {Post.objects.count()} Posts\n"
                f"   - {Favourite.objects.count()} Favourites\n"
                f"   - {Report.objects.count()} Reports\n"
                # f"   - {Image.objects.count()} Post images\n"
                f"   - {BoostRequest.objects.count()} Boost requests\n"
                f"   - {Notification.objects.count()} Notifications\n"
            )
        )