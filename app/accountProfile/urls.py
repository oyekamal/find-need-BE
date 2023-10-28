

from django.urls import path, include
from .views import LanguageViewSet, UserLanguageUpdate

from .views import CustomUserDetail, CustomUserUpdate

from .views import CountryViewSet, CityViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('country', CountryViewSet)
router.register('city', CityViewSet)
router.register('languages', LanguageViewSet)


urlpatterns = [
    path('users/languages/', UserLanguageUpdate.as_view(), name='user-language-update'),
    path('account/user/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path('account/user/update/', CustomUserUpdate.as_view(), name='user-update'),
    path('', include(router.urls)),

]
