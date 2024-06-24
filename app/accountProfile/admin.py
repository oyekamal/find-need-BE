from django.contrib import admin

from .models import Language, Country, City, CustomUser, Follow, ChatMessage, Block


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "image",
        "country",
        "created_at",
        "updated_at",
    )
    list_filter = ("country", "created_at", "updated_at")
    search_fields = ("name",)
    date_hierarchy = "created_at"


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "password",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
        "date_joined",
        "phone_number",
        "country",
        "profile_picture",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "date_joined",
        "country",
        "created_at",
        "updated_at",
    )
    raw_id_fields = ("groups", "user_permissions")
    date_hierarchy = "created_at"


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "follower", "following", "created_at")
    list_filter = ("follower", "following", "created_at")
    date_hierarchy = "created_at"


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "sender", "receiver", "message", "timestamp")
    list_filter = ("sender", "receiver", "timestamp")


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("id", "blocker", "blocked", "created_at")
    list_filter = ("blocker", "blocked", "created_at")
    date_hierarchy = "created_at"
