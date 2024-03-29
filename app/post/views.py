from rest_framework import generics, mixins

from .models import (
    Option,
    Region,
    RegionSpecs,
    PreCategory,
    Category,
    Subcategory,
    PostType,
    Image,
    Color,
    Post,
    Condition,
    Transmission,
    FuelType,
    Insurance,
    PaymentMethod,
    BoostPackage,
    Report,
    ReportChat,
    Favourite,
    Extra,
    Warranty,
)
from .serializers import (
    OptionSerializer,
    RegionSerializer,
    RegionSpecsSerializer,
    CategorySerializer,
    SubcategorySerializer,
    PostTypeSerializer,
    ImageSerializer,
    ColorSerializer,
    PostSerializer,
    PreCategorySerializer,
    ConditionSerializer,
    TransmissionSerializer,
    FuelTypeSerializer,
    InsuranceSerializer,
    PaymentMethodSerializer,
    ListCategorySerializer,
    ListSubcategorySerializer,
    ListPostTypeSerializer,
    BoostPackageSerializer,
    ListPostSerializer,
    ReportSerializer,
    ReportChatSerializer,
    ListReportSerializer,
    FavouriteSerializer,
    ExtraSerializer,
    WarrantySerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters import CharFilter, NumberFilter, ChoiceFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import DestroyModelMixin


class PageNumberPaginationCustom(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class LimitOffsetPaginationCustom(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 1000


class BoostPackageViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BoostPackage.objects.all()
    serializer_class = BoostPackageSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name", "price"]
    search_fields = ["name", "price"]


class ExtraViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class WarrantyViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class FavouriteViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["user", "post"]
    search_fields = ["user", "post"]


class ReportViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Report.objects.all()
    pagination_class = PageNumberPaginationCustom
    serializer_class = ReportSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["post", "user"]
    search_fields = ["post", "user"]

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == "list":
            return ListReportSerializer
        return ReportSerializer


class ReportChatViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ReportChat.objects.all()
    pagination_class = PageNumberPaginationCustom
    serializer_class = ReportChatSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["report", "user"]
    search_fields = ["report", "user"]


class ConditionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class TransmissionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transmission.objects.all()
    serializer_class = TransmissionSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class FuelTypeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FuelType.objects.all()
    serializer_class = FuelTypeSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class InsuranceViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class PaymentMethodViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class OptionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class RegionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class RegionSpecsViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = RegionSpecs.objects.all()
    serializer_class = RegionSpecsSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class CategoryViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name", "pre_category"]
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListCategorySerializer
        elif self.action == "retrieve":
            return ListCategorySerializer
        return CategorySerializer


class PreCategoryViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PreCategory.objects.all()
    serializer_class = PreCategorySerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class SubcategoryViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name", "category"]
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListSubcategorySerializer
        elif self.action == "retrieve":
            return ListSubcategorySerializer
        return SubcategorySerializer


class PostTypeViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name", "sub_category"]
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListPostTypeSerializer
        elif self.action == "retrieve":
            return ListPostTypeSerializer
        return PostTypeSerializer


class ImageViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["post"]


class ColorViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class PostFilter(drf_filters.FilterSet):
    title = CharFilter(lookup_expr="icontains")
    city = CharFilter(field_name="city__name", lookup_expr="icontains")
    # category = CharFilter(field_name="category__name", lookup_expr="icontains")
    price = NumberFilter(lookup_expr="lte")
    kilometers = NumberFilter(lookup_expr="lte")
    year = NumberFilter(lookup_expr="exact")
    user = NumberFilter(field_name="user__id", lookup_expr="exact")
    pre_category = NumberFilter(field_name="pre_category__id", lookup_expr="exact")
    category = NumberFilter(field_name="category__id", lookup_expr="exact")
    sub_category = NumberFilter(field_name="sub_category__id", lookup_expr="exact")
    post_type = NumberFilter(field_name="post_type__id", lookup_expr="exact")

    class Meta:
        model = Post
        fields = [
            "title",
            "city",
            "price",
            "body_condition",
            "mechanical_condition",
            "transmission",
            "fuel_type",
            "insurance",
            "payment_method",
            "kilometers",
            "year",
            "user",
            "pre_category",
            "category",
            "sub_category",
            "post_type",
        ]


class PostViewSet(ModelViewSet, DestroyModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_class = PostFilter
    search_fields = ["title", "description"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListPostSerializer
        elif self.action == "retrieve":
            return ListPostSerializer
        return PostSerializer

    pagination_class = PageNumberPaginationCustom  # Default pagination style

    def list(self, request, *args, **kwargs):
        # Determine the pagination style based on the request query parameters
        if "limit" in request.query_params and "offset" in request.query_params:
            self.pagination_class = LimitOffsetPaginationCustom
        else:
            self.pagination_class = PageNumberPaginationCustom

        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListPostSerializer(
            instance, context={"request": request}
        )  # Pass request context
        instance.view_count += 1  # Increment view_count before saving
        instance.save()  # Save the updated view_count

        return Response(serializer.data)

    def perform_destroy(self, instance):
        # Check if the delete field is already True
        if not instance.delete:
            # Soft delete by updating the 'delete' field to True
            instance.delete = True
            instance.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Post deleted Successfully."}, status=status.HTTP_204_NO_CONTENT
        )
