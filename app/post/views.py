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
    BoostRequest,
    PostExampleImage,
    ImageGroup,
    ImageGroupName,
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
    BoostRequestSerializer,
    PostExampleImageSerializer,
    ImageGroupSerializer,
    ImageGroupNameSerializer,
    ListImageGroupSerializer,
)
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters import (
    CharFilter,
    NumberFilter,
    ChoiceFilter,
    ModelChoiceFilter,
    BooleanFilter,
)

from accountProfile.serializers import DetailCountrySerializer
from accountProfile.models import Country
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import DestroyModelMixin
import random
from django.utils import timezone
from rest_framework import viewsets
from django.core.cache import cache


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


class PostExampleImageViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PostExampleImage.objects.all()
    serializer_class = PostExampleImageSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class ImageGroupNameViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ImageGroupName.objects.all()
    serializer_class = ImageGroupNameSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class ImageGroupViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ImageGroup.objects.all()
    serializer_class = ImageGroupSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["group_name"]
    search_fields = ["group_name"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListImageGroupSerializer
        elif self.action == "retrieve":
            return ListImageGroupSerializer
        return ImageGroupSerializer


class BoostRequestViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BoostRequest.objects.all()
    serializer_class = BoostRequestSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["user", "post", "boost_package"]
    search_fields = ["user", "post", "boost_package"]


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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context


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
    # city = CharFilter(field_name="city__name", lookup_expr="icontains")
    city = CharFilter(field_name="city__id", lookup_expr="exact")
    country = CharFilter(field_name="country__id", lookup_expr="exact")
    # category = CharFilter(field_name="category__name", lookup_expr="icontains")
    price = NumberFilter(lookup_expr="lte")
    price_min = drf_filters.NumberFilter(field_name="price", lookup_expr="gte")
    price_max = drf_filters.NumberFilter(field_name="price", lookup_expr="lte")
    kilometers = NumberFilter(lookup_expr="lte")
    year = NumberFilter(lookup_expr="exact")
    user = NumberFilter(field_name="user__id", lookup_expr="exact")
    pre_category = NumberFilter(field_name="pre_category__id", lookup_expr="exact")
    category = NumberFilter(field_name="category__id", lookup_expr="exact")
    sub_category = NumberFilter(field_name="sub_category__id", lookup_expr="exact")
    post_type = NumberFilter(field_name="post_type__id", lookup_expr="exact")
    # boost_package = NumberFilter(field_name="boost_package__id", lookup_expr="exact")

    boost_package = BooleanFilter(
        method="filter_boost_package"
    )  # boost_package = ModelChoiceFilter(
    #     queryset=BoostPackage.objects.all()
    # )  # Add this line
    sold = BooleanFilter(lookup_expr="exact")

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
            "price_min",
            "price_max",
            "post_type",
            "boost_package",  # Include boost_package in the fields list
            "sold",
        ]

    def filter_boost_package(self, queryset, name, value):
        """
        Filters posts based on whether `boost_package` is not null.
        """
        if value:
            return queryset.filter(boost_package__isnull=False)
        return queryset


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

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.is_authenticated:
    #         # Exclude posts from users who are blocked by the current user
    #         queryset = queryset.exclude(user__in=self.request.user.blocked_by.all())
    #     return queryset

    def get_queryset(self):
        queryset = Post.objects.all().order_by("-created_at")
        # if self.request.user.is_authenticated:
        #     # Exclude posts from users who are blocked by the current user
        #     queryset = queryset.exclude(user__in=self.request.user.blocked_by.all())
        return queryset

    def list(self, request, *args, **kwargs):
        # Determine the pagination style based on the request query parameters
        if "limit" in request.query_params and "offset" in request.query_params:
            self.pagination_class = LimitOffsetPaginationCustom
        else:
            self.pagination_class = PageNumberPaginationCustom

        response = super().list(request, *args, **kwargs)
        results = response.data.get("results", [])

        add_boost = False
        if len(request.query_params) == 0:  # if no parameters provided add boost post
            add_boost = True
        elif len(request.query_params) >= 1:
            if "offset" in request.query_params or "page" in request.query_params:
                add_boost = True

        if add_boost and "view_boost" in request.query_params:
            # Get random boosted post
            today = timezone.now()
            boosted_posts = Post.objects.filter(
                boost_package__isnull=False, expiration_date__gt=today
            ).order_by("-boost_score")

            # Insert the boosted post into the results list
            if boosted_posts:
                random_boosted_post = random.choice(boosted_posts)
                boosted_data = ListPostSerializer(
                    random_boosted_post, context={"request": request}
                ).data
                results.insert(random.randint(0, len(results)), boosted_data)

        response.data["results"] = results
        return response

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


class DetailsAPIViewSet(viewsets.ViewSet):
    def list(self, request):
        cache_key = "api_combined_data"
        combined_data = cache.get(cache_key)
        if not combined_data:
            pre_category = PreCategorySerializer(
                PreCategory.objects.all(), many=True
            ).data
            category = CategorySerializer(Category.objects.all(), many=True).data
            subcategories = ListSubcategorySerializer(
                Subcategory.objects.all(), many=True
            ).data
            post_types = PostTypeSerializer(PostType.objects.all(), many=True).data
            colors = ColorSerializer(Color.objects.all(), many=True).data
            option = OptionSerializer(Option.objects.all(), many=True).data
            region = RegionSerializer(Region.objects.all(), many=True).data
            condition = ConditionSerializer(Condition.objects.all(), many=True).data
            transmission = TransmissionSerializer(
                Transmission.objects.all(), many=True
            ).data
            fuel_type = FuelTypeSerializer(FuelType.objects.all(), many=True).data
            insureace = InsuranceSerializer(Insurance.objects.all(), many=True).data
            pyament_method = PaymentMethodSerializer(
                PaymentMethod.objects.all(), many=True
            ).data
            boost_package = BoostPackageSerializer().data
            extra = ExtraSerializer(Extra.objects.all(), many=True).data
            warranty = WarrantySerializer(Warranty.objects.all(), many=True).data
            country = DetailCountrySerializer(Country.objects.all(), many=True).data

            combined_data = {
                "pre_category": pre_category,
                "category": category,
                "subcategories": subcategories,
                "post_types": post_types,
                "colors": colors,
                "option": option,
                "region": region,
                "condition": condition,
                "transmission": transmission,
                "fuel_type": fuel_type,
                "insureace": insureace,
                "pyament_method": pyament_method,
                "boost_package": boost_package,
                "extra": extra,
                "warranty": warranty,
                "country": country,
            }

            # Set the cache
            cache.set(cache_key, combined_data, timeout=60 * 30)  # Cache for 30 minutes

        return Response(combined_data)
