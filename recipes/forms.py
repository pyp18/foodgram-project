from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from recipes.models import Ingredient, Recipe
from django.forms import ModelForm


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = (
            'title',
            'time_cooking',
            'text',
            'image',
            'tags'
        )
        labels = {
            'title': 'Название',
            'text': 'Текст',
            'ingredient': 'Ингредиенты',
            'time_cooking': 'Время приготовления',
            'tags': 'Теги',
        }

        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }


class IngredientsForm(ModelForm):

    class Meta:
        model = Ingredient
        fields = ('title', 'unit')
        labels = {'title': 'Название', 'unit': 'Единицы  измерения'}


