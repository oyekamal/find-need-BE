from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Language, CustomUser

class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=150, required=False)
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True, required=False
    )
    profile_picture = serializers.ImageField(
        max_length=None, use_url=True, required=False
    )
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
    class Meta:
        model = Language
        fields = ['id', 'name', 'flag_pictures']
        
        
class UserLanguageUpdateSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)

    class Meta:
        model = CustomUser
        fields = ['languages']

    def update(self, instance, validated_data):
        languages = validated_data.get('languages')
        instance.languages.set(languages)
        return instance


class UserSerializer(serializers.ModelSerializer):
    languages = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'languages']

