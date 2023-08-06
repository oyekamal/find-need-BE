

from django.urls import path
from .views import LanguageListCreate

urlpatterns = [
    path('languages/', LanguageListCreate.as_view(), name='language-list-create'),
]
