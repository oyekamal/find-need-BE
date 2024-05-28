from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Language, CustomUser, Country, City, Follow, Block
from django.conf import settings
from django.templatetags.static import static
from drf_extra_fields.fields import Base64ImageField


class CountrySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    # flag = serializers.SerializerMethodField()
    # name = serializers.SerializerMethodField()
    # code = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = "__all__"

    # def get_flag(self, obj):
    #     flag_path = obj.name.flag
    #     return flag_path

    # def get_name(self, obj):
    #     return obj.name.name

    # def get_code(self, obj):
    #     return obj.name.code


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=150, required=False)
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True, required=False
    )
    profile_picture = Base64ImageField(required=False)
    first_name = serializers.CharField(max_length=150, required=True)
    last_name = serializers.CharField(max_length=150, required=True)

    def custom_signup(self, request, user):
        user.phone_number = self.validated_data.get("phone_number", "")
        user.first_name = self.validated_data.get("first_name", "")
        user.last_name = self.validated_data.get("last_name", "")
        user.save()
        languages = self.validated_data.get("languages", [])
        user.languages.set(languages)
        profile_picture = self.validated_data.get("profile_picture", None)
        if profile_picture:
            user.profile_picture = profile_picture
            user.save()


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = "__all__"


class ListFollowSerializer(serializers.ModelSerializer):
    follower_username = serializers.SerializerMethodField()
    following_username = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = "__all__"
        # depth = 1

    def get_follower_username(self, obj):
        return obj.follower.username

    def get_following_username(self, obj):
        return obj.following.username


class LanguageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Language
        fields = "__all__"


class UserLanguageUpdateSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True
    )

    class Meta:
        model = CustomUser
        fields = ["languages"]

    def update(self, instance, validated_data):
        languages = validated_data.get("languages")
        instance.languages.set(languages)
        return instance


class UserSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True
    )

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "languages",
        ]


class CustomUserSerializer(serializers.ModelSerializer):
    # languages = LanguageSerializer(many=True)
    # is_following = serializers.SerializerMethodField()
    profile_picture = Base64ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "languages",
            "profile_picture",
            "created_at",
            "updated_at",
            "is_active",
            "is_staff",
            "address",
            "latitude",
            "longitude",
            "device_id",
            "country"
            # "is_following",
        ]

    # def get_is_following(self, obj):
    #     request = self.context.get('request')
    #     if request and hasattr(request, 'user'):
    #         return Follow.objects.filter(follower=request.user, following=obj).exists()
    #     return False


class GetCustomUserSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)
    follower = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    is_following = serializers.SerializerMethodField()
    country = CountrySerializer()

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "follower",
            "following",
            "last_name",
            "phone_number",
            "languages",
            "country",
            "profile_picture",
            "is_following",
            "is_active",
            "is_staff",
            "address",
            "latitude",
            "longitude",
            "device_id",
            "created_at",
            "updated_at",
        ]

    def get_is_following(self, obj):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            return Follow.objects.filter(follower=request.user, following=obj).exists()
        return False

    def get_follower(self, obj):
        # follower = Follow.objects.filter(follower=obj)
        # serializer = ListFollowSerializer(follower, many=True)
        # return serializer.data
        return Follow.objects.filter(follower=obj).count()

    def get_following(self, obj):
        # following = Follow.objects.filter(following=obj)
        # serializer = ListFollowSerializer(following, many=True)
        # return serializer.data
        return Follow.objects.filter(following=obj).count()


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "profile_picture",
        ]


class CitySerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    image = Base64ImageField(required=False)

    class Meta:
        model = City
        fields = "__all__"
        # depth = 1


class ListCitySerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    image = Base64ImageField(required=False)

    class Meta:
        model = City
        fields = "__all__"
        depth = 1


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"
