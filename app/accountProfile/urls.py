

from django.urls import path
from .views import LanguageListCreate, UserLanguageUpdate

urlpatterns = [
    path('languages/', LanguageListCreate.as_view(), name='language-list-create'),
    path('users/languages/', UserLanguageUpdate.as_view(), name='user-language-update'),
]
