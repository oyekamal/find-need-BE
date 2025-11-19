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
    """
    Custom page-based pagination for post listings.
    
    Configuration:
    - Default page size: 10 posts per page
    - Configurable via 'page_size' query parameter
    - Maximum allowed page size: 1000 posts
    
    Usage: GET /posts/?page=2&page_size=20
    """
    page_size = 10  # Default number of posts per page
    page_size_query_param = "page_size"  # Allow clients to customize page size
    max_page_size = 1000  # Prevent excessive page sizes that could impact performance


class LimitOffsetPaginationCustom(LimitOffsetPagination):
    """
    Custom offset-based pagination for post listings.
    
    Configuration:
    - Default limit: 10 posts per request
    - Configurable via 'limit' and 'offset' query parameters
    - Maximum allowed limit: 1000 posts
    
    Usage: GET /posts/?limit=20&offset=40
    """
    default_limit = 10  # Default number of posts per request
    limit_query_param = "limit"  # Parameter to specify number of posts to return
    offset_query_param = "offset"  # Parameter to specify starting position
    max_limit = 1000  # Prevent excessive limits that could impact performance


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
    filterset_fields = ["status", "post", "user"]
    search_fields = ["status", "post", "user"]

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
    filterset_fields = ["report", "user", "is_admin", "chat_type"]
    search_fields = ["report", "user", "is_admin", "chat_type"]


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
    """
    Custom filter set for Post model providing comprehensive filtering capabilities.
    Supports text search, numeric ranges, location filtering, and categorical filtering.
    """
    
    # Text-based filters - case-insensitive partial matching
    title = CharFilter(lookup_expr="icontains")  # Search within post titles
    loaction_name = CharFilter(lookup_expr="icontains")  # Search within location names
    
    # Location filters - exact ID matching for performance
    # city = CharFilter(field_name="city__name", lookup_expr="icontains")  # Deprecated: text-based city search
    city = NumberFilter(field_name="city__id", lookup_expr="exact")  # Filter by city ID
    country = NumberFilter(field_name="country__id", lookup_expr="exact")  # Filter by country ID
    
    # Price filtering - supports both single value and range filtering
    # category = CharFilter(field_name="category__name", lookup_expr="icontains")  # Deprecated: text-based category search
    price = NumberFilter(lookup_expr="lte")  # Filter posts with price less than or equal to value
    price_min = drf_filters.NumberFilter(field_name="price", lookup_expr="gte")  # Minimum price filter
    price_max = drf_filters.NumberFilter(field_name="price", lookup_expr="lte")  # Maximum price filter
    
    # Mileage/kilometers filtering - supports both single value and range
    kilometers = NumberFilter(lookup_expr="lte")  # Filter posts with kilometers less than or equal to value
    kilometer_min = drf_filters.NumberFilter(field_name="kilometers", lookup_expr="gte")  # Minimum kilometers
    kilometer_max = drf_filters.NumberFilter(field_name="kilometers", lookup_expr="lte")  # Maximum kilometers
    
    # Year filtering - supports both exact match and range filtering
    year = NumberFilter(lookup_expr="exact")  # Filter by exact year
    year_min = drf_filters.NumberFilter(field_name="year", lookup_expr="gte")  # Minimum year filter
    year_max = drf_filters.NumberFilter(field_name="year", lookup_expr="lte")  # Maximum year filter
    
    # User and category relationship filters - using foreign key IDs for performance
    user = NumberFilter(field_name="user__id", lookup_expr="exact")  # Filter posts by user ID
    pre_category = NumberFilter(field_name="pre_category__id", lookup_expr="exact")  # Filter by pre-category ID
    category = NumberFilter(field_name="category__id", lookup_expr="exact")  # Filter by category ID
    sub_category = NumberFilter(field_name="sub_category__id", lookup_expr="exact")  # Filter by subcategory ID
    post_type = NumberFilter(field_name="post_type__id", lookup_expr="exact")  # Filter by post type ID
    
    # Vehicle/product attribute filters
    color = NumberFilter(field_name="color__id", lookup_expr="exact")  # Filter by color ID
    region = NumberFilter(field_name="region__id", lookup_expr="exact")  # Filter by region ID
    region_specs = NumberFilter(field_name="region_specs__id", lookup_expr="exact")  # Filter by region specifications
    
    # Condition and technical specification filters
    body_condition = NumberFilter(field_name="body_condition__id", lookup_expr="exact")  # Filter by body condition
    mechanical_condition = NumberFilter(
        field_name="mechanical_condition__id", lookup_expr="exact"
    )  # Filter by mechanical condition
    transmission = NumberFilter(field_name="transmission__id", lookup_expr="exact")  # Filter by transmission type
    fuel_type = NumberFilter(field_name="fuel_type__id", lookup_expr="exact")  # Filter by fuel type
    insurance = NumberFilter(field_name="insurance__id", lookup_expr="exact")  # Filter by insurance type
    payment_method = NumberFilter(field_name="payment_method__id", lookup_expr="exact")  # Filter by payment method
    
    # Vehicle specification filters
    doors = CharFilter(lookup_expr="exact")  # Filter by number of doors (exact match)
    cylinders = CharFilter(lookup_expr="exact")  # Filter by number of cylinders (exact match)
    view_count = drf_filters.NumberFilter(field_name="view_count", lookup_expr="gte")  # Filter by minimum view count
    
    # Boost and status filters
    # boost_package = NumberFilter(field_name="boost_package__id", lookup_expr="exact")  # Deprecated: direct boost package filter
    is_boosted = BooleanFilter(
        method="filter_is_boosted"
    )  # Custom filter to check if post has any boost package
    # boost_package = ModelChoiceFilter(queryset=BoostPackage.objects.all())  # Alternative boost package filter
    sold = BooleanFilter(lookup_expr="exact")  # Filter by sold status

    class Meta:
        model = Post
        fields = [
            "title",
            "loaction_name",
            "city",
            "country",
            "price",
            "body_condition",
            "mechanical_condition",
            "transmission",
            "fuel_type",
            "insurance",
            "payment_method",
            "kilometers",
            "kilometer_min",
            "kilometer_max",
            "year",
            "year_min",
            "year_max",
            "user",
            "pre_category",
            "category",
            "sub_category",
            "price_min",
            "price_max",
            "post_type",
            "color",
            "is_boosted",  # Include is_boosted in the fields list
            "sold",
            "region",
            "region_specs",
            "doors",
            "cylinders",
            "view_count",
        ]

    def filter_is_boosted(self, queryset, name, value):
        """
        Custom filter method to determine if posts are boosted.
        
        Args:
            queryset: The base queryset to filter
            name: The field name (not used in this implementation)
            value: Boolean value - True to show only boosted posts, False to show all
            
        Returns:
            Filtered queryset based on boost status:
            - If value is True: returns only posts that have a boost_package assigned
            - If value is False: returns the original queryset (all posts)
        """
        if value:
            return queryset.filter(boost_package__isnull=False)  # Only boosted posts
        return queryset  # Return all posts if value is False


class PostViewSet(ModelViewSet, DestroyModelMixin):
    """
    ViewSet for managing Post objects with comprehensive CRUD operations.
    
    Features:
    - Token-based authentication required for all operations
    - Advanced filtering via PostFilter class
    - Text search in title and description fields
    - Dynamic pagination (PageNumber or LimitOffset)
    - Boost integration for promoted posts
    - Soft delete functionality
    - View count tracking on retrieve operations
    - Different serializers for list/retrieve vs create/update operations
    """
    
    authentication_classes = [TokenAuthentication]  # Require token authentication
    permission_classes = [IsAuthenticated]  # Require authenticated users
    queryset = Post.objects.all()  # Base queryset (will be modified in get_queryset)
    serializer_class = PostSerializer  # Default serializer for create/update operations
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]  # Enable search and filtering
    filterset_class = PostFilter  # Use custom filter class for advanced filtering
    search_fields = ["title", "description"]  # Enable text search in these fields

    def get_serializer_class(self):
        """
        Return appropriate serializer based on the action being performed.
        
        Returns:
            ListPostSerializer: For list and retrieve actions (read operations)
            PostSerializer: For create, update, and other write operations
        """
        if self.action == "list":
            return ListPostSerializer  # Optimized serializer for listing posts
        elif self.action == "retrieve":
            return ListPostSerializer  # Detailed serializer for single post view
        return PostSerializer  # Full serializer for create/update operations

    pagination_class = PageNumberPaginationCustom  # Default pagination style (can be overridden dynamically)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if self.request.user.is_authenticated:
    #         # Exclude posts from users who are blocked by the current user
    #         queryset = queryset.exclude(user__in=self.request.user.blocked_by.all())
    #     return queryset

    def get_queryset(self):
        """
        Get the base queryset for Post objects with custom ordering.
        
        Returns:
            QuerySet: All posts ordered by creation date (newest first)
            
        Note:
            - Posts are ordered by creation date in descending order (newest first)
            - Blocked user filtering is currently commented out but available for future use
            - The queryset will be further filtered based on request parameters via PostFilter
        """
        queryset = Post.objects.all().order_by("-created_at")  # Order by newest first
        
        # TODO: Implement user blocking functionality when required
        # if self.request.user.is_authenticated:
        #     # Exclude posts from users who are blocked by the current user
        #     queryset = queryset.exclude(user__in=self.request.user.blocked_by.all())
        
        return queryset

    def list(self, request, *args, **kwargs):
        """
        Custom list method that handles dynamic pagination and boost post injection.
        
        This method provides the main GET logic for retrieving posts with the following features:
        1. Dynamic pagination selection based on query parameters
        2. Boost post injection for promoted content visibility
        3. Smart boost insertion logic based on request context
        
        Args:
            request: HTTP request object containing query parameters
            *args, **kwargs: Additional arguments passed to the parent method
            
        Returns:
            Response: JSON response containing paginated posts with potential boost insertions
        """
        
        # STEP 1: Dynamic Pagination Selection
        # Choose pagination style based on client preferences indicated by query parameters
        if "limit" in request.query_params and "offset" in request.query_params:
            # Client prefers offset-based pagination (limit/offset style)
            self.pagination_class = LimitOffsetPaginationCustom
        else:
            # Default to page-based pagination (page number style)
            self.pagination_class = PageNumberPaginationCustom

        # STEP 2: Get Base Response
        # Call parent list method to get filtered and paginated posts
        response = super().list(request, *args, **kwargs)
        results = response.data.get("results", [])  # Extract results array from response

        # STEP 3: Boost Logic Determination
        # Decide whether to inject boosted posts based on request parameters
        add_boost = False
        
        if len(request.query_params) == 0:  
            # No filters applied - show boost posts to maximize visibility
            add_boost = True
        elif len(request.query_params) >= 1:
            # Check if boost viewing is explicitly requested
            if "view_boost" in request.query_params:
                add_boost = True
            # Or if user is just paginating through results (not filtering specifically)
            elif "offset" in request.query_params or "page" in request.query_params:
                # Count non-pagination parameters to determine if filtering is being used
                pagination_params = {"page", "page_size", "limit", "offset", "view_boost"}
                filter_params = set(request.query_params.keys()) - pagination_params
                
                # Allow boost if only pagination params or minimal filtering
                if len(filter_params) <= 2:  # Allow boost with light filtering (e.g., city + sold)
                    add_boost = True

        # STEP 4: Boost Post Injection
        # Insert random boosted post if conditions are met and boost viewing is enabled
        if add_boost and "view_boost" in request.query_params:
            
            # Get currently active boosted posts
            today = timezone.now()
            boosted_posts = Post.objects.filter(
                boost_package__isnull=False,  # Must have a boost package
                expiration_date__gt=today     # Must not be expired
            ).order_by("-boost_score")        # Order by boost score (highest priority first)

            # Insert random boosted post into results
            if boosted_posts:
                # Select random post from available boosted posts
                random_boosted_post = random.choice(boosted_posts)
                
                # Serialize the boosted post with proper context
                boosted_data = ListPostSerializer(
                    random_boosted_post, context={"request": request}
                ).data
                
                # Insert at random position to appear natural
                results.insert(random.randint(0, len(results)), boosted_data)

        # STEP 5: Return Modified Response
        # Update response with potentially modified results
        response.data["results"] = results
        return response

    def retrieve(self, request, *args, **kwargs):
        """
        Custom retrieve method for getting a single post with view count tracking.
        
        This method handles the GET request for a specific post (GET /posts/{id}/) with:
        1. Post retrieval using the provided ID
        2. Automatic view count increment for analytics
        3. Proper serialization with request context for user-specific data
        
        Args:
            request: HTTP request object
            *args, **kwargs: Additional arguments including the post ID
            
        Returns:
            Response: JSON response containing the detailed post data
            
        Side Effects:
            - Increments the view_count field of the retrieved post
            - Saves the updated post to the database
        """
        
        # STEP 1: Get Post Instance
        # Retrieve the specific post object based on the URL parameter (ID)
        instance = self.get_object()
        
        # STEP 2: Serialize Post Data
        # Use ListPostSerializer for detailed view with request context
        # Context is important for user-specific fields (like is_favorite, etc.)
        serializer = ListPostSerializer(
            instance, context={"request": request}
        )
        
        # STEP 3: Update View Analytics
        # Track post popularity by incrementing view count
        instance.view_count += 1  # Increment view counter for analytics
        instance.save()  # Persist the updated view count to database

        # STEP 4: Return Response
        return Response(serializer.data)

    def perform_destroy(self, instance):
        """
        Perform soft delete operation on a post instance.
        
        This method implements soft delete pattern where posts are marked as deleted
        rather than being permanently removed from the database. This preserves
        data integrity and allows for potential recovery operations.
        
        Args:
            instance: The Post instance to be soft deleted
            
        Note:
            - Only performs the delete operation if the post is not already marked as deleted
            - Uses the 'delete' field as a boolean flag to indicate deletion status
            - Preserves all post data and relationships in the database
        """
        
        # Check if the post is not already marked as deleted
        if not instance.delete:
            # Soft delete by updating the 'delete' field to True
            instance.delete = True
            instance.save()  # Persist the soft delete status

    def destroy(self, request, *args, **kwargs):
        """
        Handle DELETE request for posts with soft delete implementation.
        
        This method processes DELETE /posts/{id}/ requests by:
        1. Retrieving the target post instance
        2. Performing soft delete operation
        3. Returning appropriate success response
        
        Args:
            request: HTTP DELETE request object
            *args, **kwargs: Additional arguments including the post ID
            
        Returns:
            Response: Success message with HTTP 204 No Content status
            
        Note:
            - Implements soft delete pattern (marks as deleted, doesn't remove from DB)
            - Returns 204 No Content as per REST conventions for successful DELETE
        """
        
        # Get the post instance to be deleted
        instance = self.get_object()
        
        # Perform soft delete operation
        self.perform_destroy(instance)
        
        # Return success response
        return Response(
            {"message": "Post deleted Successfully."}, 
            status=status.HTTP_204_NO_CONTENT
        )


class DetailsAPIViewSet(viewsets.ViewSet):
    """
    ViewSet for providing cached lookup data for post creation and filtering.
    
    This endpoint serves as a centralized source for all the reference data needed
    by clients to create posts and populate filter dropdowns. It implements
    aggressive caching to optimize performance for frequently accessed lookup data.
    
    Endpoint: GET /details/
    Cache Duration: 30 minutes
    """
    
    def list(self, request):
        """
        Retrieve all lookup/reference data needed for post operations.
        
        This method provides a single endpoint that returns all the master data
        required for:
        - Post creation forms (categories, colors, conditions, etc.)
        - Filter dropdowns in search interfaces
        - Any UI that needs to display reference data
        
        Returns:
            Response: JSON object containing all lookup data categories
            
        Performance Features:
        - Implements 30-minute caching to reduce database queries
        - Single endpoint reduces API calls from client applications
        - Serializes all related lookup data in one response
        """
        
        # STEP 1: Check Cache
        # Use cached data if available to improve performance
        cache_key = "api_combined_data"
        combined_data = cache.get(cache_key)
        
        # STEP 2: Generate Data if Not Cached
        if not combined_data:
            # Serialize all lookup tables for post creation and filtering
            
            # Category hierarchy data
            pre_category = PreCategorySerializer(
                PreCategory.objects.all(), many=True
            ).data
            category = CategorySerializer(Category.objects.all(), many=True).data
            subcategories = ListSubcategorySerializer(
                Subcategory.objects.all(), many=True
            ).data
            post_types = PostTypeSerializer(PostType.objects.all(), many=True).data
            
            # Visual and specification attributes
            colors = ColorSerializer(Color.objects.all(), many=True).data
            option = OptionSerializer(Option.objects.all(), many=True).data
            region = RegionSerializer(Region.objects.all(), many=True).data
            condition = ConditionSerializer(Condition.objects.all(), many=True).data
            
            # Vehicle-specific attributes
            transmission = TransmissionSerializer(
                Transmission.objects.all(), many=True
            ).data
            fuel_type = FuelTypeSerializer(FuelType.objects.all(), many=True).data
            insureace = InsuranceSerializer(Insurance.objects.all(), many=True).data
            pyament_method = PaymentMethodSerializer(
                PaymentMethod.objects.all(), many=True
            ).data
            
            # Business and service attributes
            boost_package = BoostPackageSerializer().data  # Promotion packages
            extra = ExtraSerializer(Extra.objects.all(), many=True).data  # Additional features
            warranty = WarrantySerializer(Warranty.objects.all(), many=True).data  # Warranty options
            country = DetailCountrySerializer(Country.objects.all(), many=True).data  # Location data

            # STEP 3: Combine All Data
            # Structure all lookup data into a single response object
            combined_data = {
                "pre_category": pre_category,      # Top-level categories
                "category": category,              # Main categories
                "subcategories": subcategories,   # Sub-categories
                "post_types": post_types,          # Specific post types
                "colors": colors,                  # Available colors
                "option": option,                  # General options
                "region": region,                  # Geographic regions
                "condition": condition,            # Condition states
                "transmission": transmission,      # Transmission types
                "fuel_type": fuel_type,           # Fuel types
                "insureace": insureace,           # Insurance options
                "pyament_method": pyament_method, # Payment methods
                "boost_package": boost_package,   # Promotion packages
                "extra": extra,                   # Extra features
                "warranty": warranty,             # Warranty options
                "country": country,               # Countries and cities
            }

            # STEP 4: Cache the Data
            # Store in cache for 30 minutes to improve subsequent request performance
            cache.set(cache_key, combined_data, timeout=60 * 30)  # Cache for 30 minutes

        # STEP 5: Return Response
        return Response(combined_data)
