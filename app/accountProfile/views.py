from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, LanguageSerializer, UserLanguageUpdateSerializer, UserSerializer, CustomUserUpdateSerializer
from .models import Language, CustomUser, Country, City
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CountrySerializer, CitySerializer
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from .serializers import CustomUserSerializer


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "User created successfully."}, status=201, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Additional logic if needed


class LanguageViewSet(ModelViewSet):
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
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updated_instance = self.get_object()  # Get the updated user instance
        return Response(UserSerializer(updated_instance).data, status=status.HTTP_200_OK)


class CustomUserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ['name', 'country']
