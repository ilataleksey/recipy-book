from .models import Recipes
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class RecipesForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта',
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс рецепта',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание рецепта',
            }),
        }
