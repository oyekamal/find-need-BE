from django.contrib import admin
from .models import Language, CustomUser, Country, City

# Register your models here.
admin.site.register(Language)
admin.site.register(CustomUser)
admin.site.register(Country)
admin.site.register(City)
