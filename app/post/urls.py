from django.urls import path, include
from .views import (
    ColorViewSet,
    ImageViewSet,
    PostViewSet,
    OptionViewSet,
    RegionViewSet,
    RegionSpecsViewSet,
    CategoryViewSet,
    SubcategoryViewSet,
    PostTypeViewSet,
    PreCategoryViewSet,
    ConditionViewSet,
    TransmissionViewSet,
    FuelTypeViewSet,
    InsuranceViewSet,
    PaymentMethodViewSet,
    BoostPackageViewSet,
    ReportViewSet,
    ReportChatViewSet,
    FavouriteViewSet,
    ExtraViewSet,
    WarrantyViewSet,
    BoostRequestViewSet,
    PostExampleImageViewSet,
    ImageGroupViewSet,
    ImageGroupNameViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("extra", ExtraViewSet)
router.register("warranty", WarrantyViewSet)
router.register("favourite", FavouriteViewSet)
router.register("favourite", FavouriteViewSet)
router.register("posts", PostViewSet)
router.register("option", OptionViewSet)
router.register("region", RegionViewSet)
router.register("region_specs", RegionSpecsViewSet)
router.register("preCategory", PreCategoryViewSet)
router.register("category", CategoryViewSet)
router.register("subcategory", SubcategoryViewSet)
router.register("posttype", PostTypeViewSet)
router.register("image", ImageViewSet)
router.register("color", ColorViewSet)
router.register("condition", ConditionViewSet)
router.register("transmission", TransmissionViewSet)
router.register("fuel_type", FuelTypeViewSet)
router.register("insurance", InsuranceViewSet)
router.register("payment_method", PaymentMethodViewSet)
router.register("boost_package", BoostPackageViewSet)
router.register("boost_request", BoostRequestViewSet)
router.register("report", ReportViewSet)
router.register("report_chat", ReportChatViewSet)
router.register("post_example_image", PostExampleImageViewSet)
router.register("image_group", ImageGroupViewSet)
router.register("image_group_name", ImageGroupNameViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
