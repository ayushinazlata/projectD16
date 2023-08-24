from django.forms import DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateFilter
from .models import Post, Category
from django.utils.translation import gettext_lazy as _


class AdvertFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label=_('Категория'),
        empty_label=_('выберите категорию'),
    )

    date_creation_after = DateFilter(
        field_name='created_at',
        label=_('Публикации от'),
        lookup_expr='gt',
        widget=DateInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = [
            'title',
        ]
        labels = {
            'title': _('Заголовок'),
        }


class UserAdvertFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label=_('Категория'),
        empty_label=_('выберите категорию'),
    )

    date_creation_after = DateFilter(
        field_name='created_at',
        label=_('Публикации от'),
        lookup_expr='gt',
        widget=DateInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'},
        ),
    )


class ReactionFilter(FilterSet):
    post = ModelChoiceFilter(
        field_name='post',
        queryset=Post.objects.all(),
        label=_('Объявление'),
        empty_label=_('выберите объявление'),
    )

    date_creation_after = DateFilter(
        field_name='created_at',
        label=_('Публикации от'),
        lookup_expr='gt',
        widget=DateInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'},
        ),
    )


