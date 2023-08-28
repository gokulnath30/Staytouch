from django_filters import rest_framework as filters
from .models import Business


# We create filters for each field we want to be able to filter on
class BusinessFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr='icontains')
    ratings = filters.CharFilter(lookup_expr='icontains')
    location = filters.CharFilter(lookup_expr='icontains')
    creator__username = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Business
        fields = ['category', 'ratings', 'location', 'creator__username']

