from django.contrib import admin

from .models import Image, Option, Region, Category, CarMaker, CarModel, VehiclePost


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


@admin.register(CarMaker)
class CarMakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name')
    search_fields = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'maker', 'name')
    list_filter = ('maker',)
    search_fields = ('name',)


@admin.register(VehiclePost)
class VehiclePostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'city',
        'category',
        'car_maker',
        'car_model',
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
        'car_maker',
        'car_model',
        'region',
    )
    raw_id_fields = ('images', 'options')