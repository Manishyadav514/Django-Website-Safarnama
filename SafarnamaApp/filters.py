import django_filters
from .models import super
from .models import *

class SuperFilter(django_filters.FilterSet):
    class Meta:
         model = super
         fields = ['city', 'hotel']