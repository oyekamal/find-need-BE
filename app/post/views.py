from rest_framework import generics, mixins

from .models import Option, Region, Category, Subcategory, PostType, Image, Color, Post
from .serializers import OptionSerializer, RegionSerializer, CategorySerializer, SubcategorySerializer, PostTypeSerializer, ImageSerializer, ColorSerializer, PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters import CharFilter, NumberFilter, ChoiceFilter

class OptionListDetail(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin):
    serializer_class = OptionSerializer
    queryset = Option.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class RegionListDetail(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

# Repeat this pattern for all other models.


class CategoryListDetail(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class SubcategoryListDetail(generics.GenericAPIView,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class PostTypeListDetail(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    serializer_class = PostTypeSerializer
    queryset = PostType.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)


class ColorListDetail(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    serializer_class = ColorSerializer
    queryset = Color.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
        

class PostFilter(drf_filters.FilterSet):
    title = CharFilter(lookup_expr='icontains')
    city = CharFilter(field_name='city__name', lookup_expr='icontains')
    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    price = NumberFilter(lookup_expr='lte')
    body_condition = ChoiceFilter(choices=Post.CONDITION_CHOICES)
    mechanical_condition = ChoiceFilter(choices=Post.CONDITION_CHOICES)
    transmission = ChoiceFilter(choices=Post.TRANSMISSION_CHOICES)
    fuel_type = ChoiceFilter(choices=Post.FUEL_CHOICES)
    insurance = ChoiceFilter(choices=Post.INSURANCE_CHOICES)
    payment_method = ChoiceFilter(choices=Post.PAYMENT_METHOD_CHOICES)
    kilometers = NumberFilter(lookup_expr='lte')
    year = NumberFilter(lookup_expr='exact')

    class Meta:
        model = Post
        fields = ['title', 'city', 'category', 'price', 'body_condition', 'mechanical_condition', 'transmission', 'fuel_type', 'insurance', 'payment_method', 'kilometers', 'year']



class PageNumberPaginationCustom(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class LimitOffsetPaginationCustom(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 1000

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_class = PostFilter
    search_fields = ['title', 'description']

    pagination_class = PageNumberPaginationCustom  # Default pagination style

    def list(self, request, *args, **kwargs):
        # Determine the pagination style based on the request query parameters
        if 'limit' in request.query_params and 'offset' in request.query_params:
            self.pagination_class = LimitOffsetPaginationCustom
        else:
            self.pagination_class = PageNumberPaginationCustom

        return super().list(request, *args, **kwargs)


