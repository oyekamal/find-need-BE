from django.urls import path, include
from .views import (
    ColorViewSet,
    ImageViewSet,
    PostViewSet,
    OptionViewSet,
    RegionViewSet,
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
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("posts", PostViewSet)
router.register("option", OptionViewSet)
router.register("region", RegionViewSet)
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
router.register("report", ReportViewSet)
router.register("report_chat", ReportChatViewSet)



urlpatterns = [
    path("", include(router.urls)),
]
