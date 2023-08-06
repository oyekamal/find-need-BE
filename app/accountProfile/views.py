from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, LanguageSerializer
from .models import Language
from rest_framework import generics
from rest_framework.permissions import AllowAny

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

class LanguageListCreate(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny]
