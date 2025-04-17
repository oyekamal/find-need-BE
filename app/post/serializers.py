from rest_framework import serializers
from .models import (
    Option,
    Region,
    RegionSpecs,
    PreCategory,
    Category,
    StripePaymentIntent,
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
    Report,
    ReportChat,
    Favourite,
    Extra,
    Warranty,
    BoostRequest,
    PostExampleImage,
    ImageGroup,
    ImageGroupName,
)
from drf_extra_fields.fields import Base64ImageField
from accountProfile.serializers import (
    CustomUserSerializer,
    ListCitySerializer,
    GetCustomUserSerializer,
)


class PostExampleImageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = PostExampleImage
        fields = "__all__"


class ImageGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGroup
        fields = "__all__"


class ImageGroupNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGroupName
        fields = "__all__"


class ListImageGroupNameSerializer(serializers.ModelSerializer):
    post_example_images = serializers.SerializerMethodField()

    class Meta:
        model = ImageGroupName
        fields = "__all__"

    def get_post_example_images(self, obj):
        """
        Return all related PostExampleImage instances for the category.
        """
        # Assuming there's a direct relation between Category and PostExampleImage,
        # adjust the query accordingly if the relation is indirect or requires filtering.
        image_groups = ImageGroup.objects.filter(group_name=obj)
        # Extract unique PostExampleImage IDs from the filtered ImageGroups
        post_example_image_ids = set(
            image_group.image.id for image_group in image_groups
        )

        # Fetch the PostExampleImage instances using the extracted IDs
        post_example_images = PostExampleImage.objects.filter(
            id__in=post_example_image_ids
        )
        # post_example_images = obj.postexampleimage_set.all()
        return PostExampleImageSerializer(post_example_images, many=True).data


class ListImageGroupSerializer(serializers.ModelSerializer):
    group_name = ImageGroupNameSerializer()
    image = PostExampleImageSerializer()

    class Meta:
        model = ImageGroup
        fields = "__all__"


class BoostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoostRequest
        fields = "__all__"


class ReportChatSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = ReportChat
        fields = "__all__"


class WarrantySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Warranty
        fields = "__all__"


class ExtraSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Extra
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = "__all__"


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


class RegionSpecsSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = RegionSpecs
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
    group_name = ListImageGroupNameSerializer()

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


class ListPostSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    user = GetCustomUserSerializer()
    city = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    pre_category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()
    post_type = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    body_condition = serializers.SerializerMethodField()
    mechanical_condition = serializers.SerializerMethodField()
    transmission = serializers.SerializerMethodField()
    fuel_type = serializers.SerializerMethodField()
    insurance = serializers.SerializerMethodField()
    payment_method = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    boost_package = BoostPackageSerializer()
    images = serializers.SerializerMethodField()
    options = OptionSerializer(many=True)
    extra = ExtraSerializer(many=True)
    favourite = serializers.SerializerMethodField()
    warranty = WarrantySerializer()

    # New field to indicate whether the post is boosted/premium
    boost_status = serializers.SerializerMethodField()

    # New method to determine boost status
    def get_boost_status(self, obj):
        if obj.boost_package:
            return "PREMIUM"  # or "PREMIUM" if preferred
        return "STANDARD"

    def get_favourite(self, obj):
        request = self.context.get("request")
        if request.user.is_authenticated:
            return Favourite.objects.filter(user=request.user, post=obj).exists()
        return False  # Return False if user is not authenticated

    def get_category(self, obj):
        if obj.category:
            return obj.category.name
        else:
            return None

    def get_pre_category(self, obj):
        if obj.pre_category:
            return obj.pre_category.name
        else:
            return None

    def get_sub_category(self, obj):
        if obj.sub_category:
            return obj.sub_category.name
        else:
            return None

    def get_post_type(self, obj):
        if obj.post_type:
            return obj.post_type.name
        else:
            return None

    def get_region(self, obj):
        if obj.region:
            return obj.region.name
        else:
            return None

    def get_body_condition(self, obj):
        if obj.body_condition:
            return obj.body_condition.name
        else:
            return None

    def get_mechanical_condition(self, obj):
        if obj.mechanical_condition:
            return obj.mechanical_condition.name
        else:
            return None

    def get_city(self, obj):
        if obj.city:
            return obj.city.name
        else:
            return None

    def get_country(self, obj):
        if obj.country:
            return obj.country.name
        else:
            return None

    def get_transmission(self, obj):
        if obj.transmission:
            return obj.transmission.name
        else:
            return None

    def get_fuel_type(self, obj):
        if obj.fuel_type:
            return obj.fuel_type.name
        else:
            return None

    def get_insurance(self, obj):
        if obj.insurance:
            return obj.insurance.name
        else:
            return None

    def get_payment_method(self, obj):
        if obj.payment_method:
            return obj.payment_method.name
        else:
            return None

    def get_color(self, obj):
        if obj.color:
            return obj.color.name
        else:
            return None

    def get_images(self, obj):
        Images = Image.objects.filter(post=obj)
        serializer = ImageSerializer(Images, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = "__all__"
        # fields = ("id", "boost_package", "boost_score", "created_at", "view_count", "favourite")
        # depth = 1


class ListReportSerializer(serializers.ModelSerializer):

    post = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    # user = CustomUserSerializer()

    def get_post(self, obj):
        # Access the request from the serializer's context
        request = self.context.get("request")
        # Pass the request to ListPostSerializer
        serializer = ListPostSerializer(obj.post, context={"request": request})
        return serializer.data

    def get_user(self, obj):
        if obj.user:
            serializer = GetCustomUserSerializer(obj.user)
            return serializer.data

    class Meta:
        model = Report
        fields = "__all__"
        # depth = 1


class CreatePaymentIntentSerializer(serializers.Serializer):
    boost_package_id = serializers.IntegerField()
    post_id = serializers.IntegerField()


class PaymentIntentResponseSerializer(serializers.ModelSerializer):
    client_secret = serializers.CharField(read_only=True)

    class Meta:
        model = StripePaymentIntent
        fields = ["id", "amount", "currency", "status", "client_secret"]
