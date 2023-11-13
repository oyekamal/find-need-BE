from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Language, CustomUser, Country, City
from django.conf import settings
from django.templatetags.static import static
from drf_extra_fields.fields import Base64ImageField


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


class LanguageSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Language
        fields = "__all__"


class UserLanguageUpdateSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True)

    class Meta:
        model = CustomUser
        fields = ['languages']

    def update(self, instance, validated_data):
        languages = validated_data.get('languages')
        instance.languages.set(languages)
        return instance


class UserSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name',
                  'last_name', 'phone_number', 'languages']


class CustomUserSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name',
                  'last_name', 'phone_number', 'languages', 'profile_picture']


class CustomUserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name',
                  'last_name', 'phone_number', 'profile_picture']


class CountrySerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    # flag = serializers.SerializerMethodField()
    # name = serializers.SerializerMethodField()
    # code = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = '__all__'

    # def get_flag(self, obj):
    #     flag_path = obj.name.flag
    #     return flag_path

    # def get_name(self, obj):
    #     return obj.name.name

    # def get_code(self, obj):
    #     return obj.name.code


class CitySerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    image = Base64ImageField(required=False)

    class Meta:
        model = City
        fields = '__all__'
        # depth = 1
