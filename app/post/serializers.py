from rest_framework import serializers
from .models import (Option, Region, 
                     PreCategory, Category, Subcategory, 
                     PostType, Image, Color, Post,
                     Condition, Transmission, FuelType,Insurance,PaymentMethod)


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = '__all__'

class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
        

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class PreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PreCategory
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'
        depth = 1

class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = '__all__'
        depth = 2

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth = 2