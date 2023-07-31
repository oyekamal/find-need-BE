from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Language

class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=150, required=False)
    languages = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), many=True, required=False
    )
    profile_picture = serializers.ImageField(
        max_length=None, use_url=True, required=False
    )

    def custom_signup(self, request, user):
        user.phone_number = self.validated_data.get("phone_number", "")
        user.save()
        languages = self.validated_data.get("languages", [])
        user.languages.set(languages)
        profile_picture = self.validated_data.get("profile_picture", None)
        if profile_picture:
            user.profile_picture = profile_picture
            user.save()
