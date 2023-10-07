from django.urls import path, include
from .views import (ColorViewSet, ImageViewSet, 
                    PostViewSet, OptionViewSet, RegionViewSet, 
                    CategoryViewSet, SubcategoryViewSet, PostTypeViewSet,
                    PreCategoryViewSet)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('option', OptionViewSet)
router.register('region', RegionViewSet)
router.register('preCategory', PreCategoryViewSet)
router.register('category', CategoryViewSet)
router.register('subcategory', SubcategoryViewSet)
router.register('posttype', PostTypeViewSet)
router.register('image', ImageViewSet)
router.register('color', ColorViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
