from django.urls import path, include
from .views import OptionListDetail, RegionListDetail, CategoryListDetail, SubcategoryListDetail, PostTypeListDetail, ColorListDetail, PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('option/', OptionListDetail.as_view(), name='option-detail'),
    path('option/<int:id>/', OptionListDetail.as_view(), name='option_detail'),
    path('region/', RegionListDetail.as_view(), name='region_list'),
    path('region/<int:id>/', RegionListDetail.as_view(), name='region_detail'),
    path('category/', CategoryListDetail.as_view(), name='category_list'),
    path('category/<int:id>/', CategoryListDetail.as_view(), name='category_detail'),
    path('subcategory/', SubcategoryListDetail.as_view(), name='subcategory_list'),
    path('subcategory/<int:id>/', SubcategoryListDetail.as_view(),
         name='subcategory_detail'),
    path('posttype/', PostTypeListDetail.as_view(), name='posttype_list'),
    path('posttype/<int:id>/', PostTypeListDetail.as_view(), name='posttype_detail'),
    path('color/', ColorListDetail.as_view(), name='Color_list'),
    path('color/<int:id>/', ColorListDetail.as_view(), name='Color_detail'),
]
