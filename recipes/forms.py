from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from recipes.models import Ingredient, Recipe
from django.forms import ModelForm

User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')
