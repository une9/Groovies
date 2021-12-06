from django_filters.filters import CharFilter
from .models import Movie
from django_filters import FilterSet


# 검색 필터
class MovieSearchFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')
    original_title = CharFilter(lookup_expr='icontains')
    tagline = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ('title', 'original_title', 'tagline',)







# class MovieSearchFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     original_title = django_filters.CharFilter(lookup_expr='icontains')
#     tagline = django_filters.CharFilter(lookup_expr='icontains')

#     class Meta:
#         model = Movie
#         fields = ['title', 'original_title', 'tagline']