from django import forms
from django.core.exceptions import ValidationError

from tinymce.widgets import TinyMCE

from .models import Post, Category, Reaction
from django.utils.translation import gettext_lazy as _


class AdvertsForm(forms.ModelForm):
    attachments = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=_('Текст объявления'))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label=_('Категория'),
                                      empty_label='выберите категорию')
    title = forms.CharField(max_length=255, label=_('Заголовок'), widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = Post
        fields = [
            'title',
            'attachments',
            'category',
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы."
            )

        text = cleaned_data.get("text")
        if title == text:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )
        return cleaned_data


class ReactionForm(forms.ModelForm):
    text = forms.CharField(max_length=255, label=_('Текст'))

    class Meta:
        model = Reaction
        fields = [
            'text',
        ]

