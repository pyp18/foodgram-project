from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
# Create your models here.
User = get_user_model()

class Tag(models.Model):
    class ChoiceTag(models.TextChoices):
        breakfast = 'Завтрак'
        lunch = 'Обед'
        dinner = 'Ужин'

    title = models.CharField(
        max_length=100,
        unique=True,
        choices=ChoiceTag.choices
    )

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    unit = models.CharField(max_length=150, verbose_name='Единицы измерения')

    class Meta:
        ordering = ('title', )
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f"{self.title}, {self.unit}"


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Название рецепта')
    image = models.ImageField(upload_to="images/", blank=True, null=True, verbose_name='Картинка')
    text = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='tag')
    time_cooking = models.PositiveIntegerField()
    slug = models.SlugField(max_length=40, unique=True)
    ingredient = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=CASCADE)
    Ingredient = models.ForeignKey(Ingredient, on_delete=CASCADE)
    count = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.Ingredient}, {self.recipe}"



class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, related_name = 'favourites', verbose_name = 'пользователь')
    recipe = models.ForeignKey(Recipe, on_delete=CASCADE, related_name = 'favourites', verbose_name = 'рецепт')

    def __str__(self):
        return f'Избранный {self.recipe} у {self.user}'