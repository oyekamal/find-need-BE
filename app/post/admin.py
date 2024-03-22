from django.contrib import admin

from .models import (
    Image,
    Condition,
    Transmission,
    FuelType,
    Insurance,
    PaymentMethod,
    Option,
    Extra,
    Region,
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
    ReportChat,
)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "image", "created_at", "updated_at")
    list_filter = ("post", "created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Insurance)
class InsuranceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "name", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(PreCategory)
class PreCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "name",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "name",
        "pre_category",
        "created_at",
        "updated_at",
    )
    list_filter = ("pre_category", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "name",
        "category",
        "created_at",
        "updated_at",
    )
    list_filter = ("category", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image",
        "sub_category",
        "name",
        "created_at",
        "updated_at",
    )
    list_filter = ("sub_category", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(BoostPackage)
class BoostPackageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "duration_days",
        "price",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "city",
        "pre_category",
        "category",
        "sub_category",
        "post_type",
        "year",
        "region",
        "body_condition",
        "mechanical_condition",
        "transmission",
        "fuel_type",
        "insurance",
        "payment_method",
        "kilometers",
        "color",
        "warranty",
        "title",
        "description",
        "price",
        "phone_number",
        "boost_package",
        "boost_score",
        "expiration_date",
        "view_count",
        "doors",
        "cylinders",
        "latitude",
        "longitude",
        "loaction_name",
        "created_at",
        "updated_at",
        "delete",
    )
    list_filter = (
        "user",
        "city",
        "pre_category",
        "category",
        "sub_category",
        "post_type",
        "region",
        "body_condition",
        "mechanical_condition",
        "transmission",
        "fuel_type",
        "insurance",
        "payment_method",
        "color",
        "warranty",
        "boost_package",
        "expiration_date",
        "created_at",
        "updated_at",
        "delete",
    )
    # raw_id_fields = ("options", "extra")
    date_hierarchy = "created_at"


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_at", "updated_at")
    list_filter = ("user", "post", "created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "reason", "created_at", "status")
    list_filter = ("post", "user", "created_at")
    date_hierarchy = "created_at"


@admin.register(ReportChat)
class ReportChatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "report",
        "user",
        "message",
        "image",
        "audio",
        "is_admin",
        "created_at",
    )
    list_filter = ("report", "user", "is_admin", "created_at")
    date_hierarchy = "created_at"
