from rest_framework import generics, mixins

from .models import Option, Region, Category, Subcategory, PostType, Image, Color
from .serializers import OptionSerializer, RegionSerializer, CategorySerializer, SubcategorySerializer, PostTypeSerializer, ImageSerializer, ColorSerializer
from django.shortcuts import get_object_or_404


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
