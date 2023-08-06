from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, LanguageSerializer, UserLanguageUpdateSerializer, UserSerializer
from .models import Language, CustomUser
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

class LanguageListCreate(generics.ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny]


class UserLanguageUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLanguageUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updated_instance = self.get_object()  # Get the updated user instance
        return Response(UserSerializer(updated_instance).data, status=status.HTTP_200_OK)
