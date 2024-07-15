from django.urls import path, include
from .views import LanguageViewSet, UserLanguageUpdate

from .views import CustomUserDetail, CustomUserUpdate

from .views import (
    CountryViewSet,
    CityViewSet,
    CustomLoginView,
    FollowViewSet,
    FollowerListView,
    FollowingListView,
    BlockViewSet,
    ChatMessageViewSet,
    NotificationViewSet,
)

from rest_framework.routers import DefaultRouter
from dj_rest_auth.views import LoginView


router = DefaultRouter()
router.register("country", CountryViewSet)
router.register("city", CityViewSet)
router.register("languages", LanguageViewSet)
router.register("user", CustomUserDetail)
router.register("follow", FollowViewSet)
router.register(r"blocks", BlockViewSet)
router.register("chat", ChatMessageViewSet)
router.register("notification", NotificationViewSet)


urlpatterns = [
    path("account/login/", CustomLoginView.as_view(), name="rest_login"),
    path("users/languages/", UserLanguageUpdate.as_view(), name="user-language-update"),
    # path('account/user/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path("account/user/update/", CustomUserUpdate.as_view(), name="user-update"),
    path("followers/<int:user_id>/", FollowerListView.as_view(), name="follower-list"),
    path(
        "following/<int:user_id>/", FollowingListView.as_view(), name="following-list"
    ),
    path("", include(router.urls)),
]
