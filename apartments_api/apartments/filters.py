import django_filters
from .models import ApartmentModel


class ApartFilter(django_filters.FilterSet):
    class Meta:
        model = ApartmentModel
        fields = {
            'title': ['iexact', 'contains'],
            'price': ['lt', 'gt'],
        }
