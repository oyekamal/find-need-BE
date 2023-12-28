from rest_framework import serializers
from .models import (
    Option,
    Region,
    PreCategory,
    Category,
    Subcategory,
    PostType,
    Image,
    Color,
    Post,
    Condition,
    Transmission,
    FuelType,
    Insurance,
    PaymentMethod,
    BoostPackage,
)
from drf_extra_fields.fields import Base64ImageField


class BoostPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoostPackage
        fields = "__all__"


class ConditionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Condition
        fields = "__all__"


class TransmissionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Transmission
        fields = "__all__"


class FuelTypeSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = FuelType
        fields = "__all__"


class InsuranceSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Insurance
        fields = "__all__"


class PaymentMethodSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = PaymentMethod
        fields = "__all__"


class OptionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Option
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Region
        fields = "__all__"


class PreCategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = PreCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Category
        fields = "__all__"


class ListCategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Category
        fields = "__all__"
        depth = 1


class SubcategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Subcategory
        fields = "__all__"
        # depth = 1


class ListSubcategorySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Subcategory
        fields = "__all__"
        depth = 1


class PostTypeSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = PostType
        fields = "__all__"
        # depth = 2


class ListPostTypeSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = PostType
        fields = "__all__"
        depth = 1


class ImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Image
        fields = "__all__"


class ColorSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Color
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        # depth = 2
