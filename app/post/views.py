from rest_framework import generics, mixins

from .models import (Option, Region, 
                     PreCategory, Category, Subcategory, 
                     PostType, Image, Color, Post,
                     Condition, Transmission, FuelType,Insurance,PaymentMethod)
from .serializers import (OptionSerializer, RegionSerializer, CategorySerializer, SubcategorySerializer, 
                          PostTypeSerializer, ImageSerializer, ColorSerializer, PostSerializer,
                          PreCategorySerializer)
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters import CharFilter, NumberFilter, ChoiceFilter

class OptionViewSet(ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    
class RegionViewSet(ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class PreCategoryViewSet(ModelViewSet):
    queryset = PreCategory.objects.all()
    serializer_class = PreCategorySerializer
      

class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    
    
class PostTypeViewSet(ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
      

class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
      
      
class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
      
      
class PostFilter(drf_filters.FilterSet):
    title = CharFilter(lookup_expr='icontains')
    city = CharFilter(field_name='city__name', lookup_expr='icontains')
    category = CharFilter(field_name='category__name', lookup_expr='icontains')
    price = NumberFilter(lookup_expr='lte')
    # body_condition = ChoiceFilter(choices=Post.CONDITION_CHOICES)
    # mechanical_condition = ChoiceFilter(choices=Post.CONDITION_CHOICES)
    # transmission = ChoiceFilter(choices=Post.TRANSMISSION_CHOICES)
    # fuel_type = ChoiceFilter(choices=Post.FUEL_CHOICES)
    # insurance = ChoiceFilter(choices=Post.INSURANCE_CHOICES)
    # payment_method = ChoiceFilter(choices=Post.PAYMENT_METHOD_CHOICES)
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


