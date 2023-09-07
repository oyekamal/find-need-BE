from django.contrib import admin

from .models import Image, Option, Region, Category, Color, Subcategory, PostType, Post


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name')
    search_fields = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'sub_category', 'name')
    list_filter = ('sub_category',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'city',
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
    )
    list_filter = (
        'user',
        'city',
        'category',
        'sub_category',
        'post_type',
        'region',
        'color',
    )
    raw_id_fields = ('images', 'options')