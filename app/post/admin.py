from django.contrib import admin

from .models import Image, Option, Region, PreCategory, Category, Color, Subcategory, PostType, BoostPackage, Post


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(PreCategory)
class PreCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'name',
        'pre_category',
        'created_at',
        'updated_at',
    )
    list_filter = ('pre_category', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'name',
        'category',
        'created_at',
        'updated_at',
    )
    list_filter = ('category', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'image',
        'sub_category',
        'name',
        'created_at',
        'updated_at',
    )
    list_filter = ('sub_category', 'created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(BoostPackage)
class BoostPackageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'duration_days',
        'price',
        'created_at',
        'updated_at',
    )
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'city',
        'pre_category',
        'category',
        'sub_category',
        'post_type',
        'year',
        'region',
        'body_condition',
        'mechanical_condition',
        'kilometers',
        'transmission',
        'fuel_type',
        'insurance',
        'color',
        'payment_method',
        'title',
        'description',
        'price',
        'phone_number',
        'boost_package',
        'boost_score',
        'expiration_date',
        'view_count',
        'latitude',
        'longitude',
        'loaction_name',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'user',
        'city',
        'pre_category',
        'category',
        'sub_category',
        'post_type',
        'region',
        'color',
        'boost_package',
        'expiration_date',
        'created_at',
        'updated_at',
    )
    raw_id_fields = ('images', 'options')
    date_hierarchy = 'created_at'