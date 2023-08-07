

from django.urls import path
from .views import LanguageListCreate, UserLanguageUpdate

from .views import CustomUserDetail, CustomUserUpdate



urlpatterns = [
    path('languages/', LanguageListCreate.as_view(), name='language-list-create'),
    path('users/languages/', UserLanguageUpdate.as_view(), name='user-language-update'),
    path('account/user/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),
    path('account/user/update/', CustomUserUpdate.as_view(), name='user-update'),
]
