"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from accountProfile.views import CustomRegisterView
from django.conf import settings
from django.conf.urls.static import static

# urls.py

from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from django.urls import path, include, re_path


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class GoogleLoginAPIView(APIView):
    def validate_access_token(self, access_token):
        url = f"https://oauth2.googleapis.com/tokeninfo?access_token={access_token}"
        response = requests.get(url)
        return response.json()

    def post(self, request):
        access_token = request.data.get("access_token")
        if not access_token:
            return Response(
                {"error": "Access token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        token_info = self.validate_access_token(access_token)
        # Check if the token is valid and contains the required information
        if "sub" in token_info:
            # Extract user info
            user_id = token_info["sub"]
            email = token_info.get("email")
            # Get or create the user
            user, created = User.objects.get_or_create(
                username=user_id, defaults={"email": email}
            )
            # Generate or retrieve the auth token
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid access token."}, status=status.HTTP_401_UNAUTHORIZED
            )


schema_view = get_schema_view(
    openapi.Info(
        title="Find-need",
        default_version="v1",
        description="Find-need backend in django.",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("accountProfile.urls")),
    path("accounts/", include("allauth.urls")),
    path("account/", include("dj_rest_auth.urls")),
    path("api/google-login/", GoogleLoginAPIView.as_view(), name="google-login"),
    path("", include("post.urls")),
    # path('account/registration/', include('dj_rest_auth.registration.urls')),
    path("account/registration/", CustomRegisterView.as_view(), name="custom_register"),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    re_path(
        r"^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
