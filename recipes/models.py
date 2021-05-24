from typing import Optional
from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Exists
from django.db.models import OuterRef, Exists
# Create your models here.
User = get_user_model()


class RecipeQuerySet(models.QuerySet):
    def with_is_favorite(self, user_id: Optional[int]):
        return self.annotate(is_favorite=Exists(
            Favorite.objects.filter(
                user_id=user_id,
                recipe_id=OuterRef('pk'),
            ),
        ))


class Tag(models.Model):

    MEALS = (
        ('Завтрак', 'breakfast'),
        ('Обед', 'lunch'),
        ('Ужин', 'dinner'),
    )
    title = models.CharField(
        verbose_name='Название тега',
        max_length=100,
        unique=True,
        choices=MEALS
    )
    display_name = models.CharField(
        max_length=20, verbose_name='Имя тега в шаблоне', default='Name')
    color = models.CharField(
        max_length=50, verbose_name='Цвет тега', default="Red")

    def __str__(self):
        return f'{self.title}'


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
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes', verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Название рецепта')
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name='Картинка')
    text = models.TextField(verbose_name='Описание')
    tags = models.ManyToManyField(Tag, related_name='tags')
    time_cooking = models.PositiveIntegerField()
    slug = models.SlugField(max_length=40, unique=False)
    ingredient = models.ManyToManyField(Ingredient, through="RecipeIngredient")
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    objects = RecipeQuerySet.as_manager()

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.ingredient}, {self.recipe}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites', verbose_name='пользователь')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorites', verbose_name='рецепт')

    def __str__(self):
        return f'Избранный {self.recipe} у {self.user}'


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follower")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following")

    class Meta:
        unique_together = ["author", "user"]
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'{self.user} на {self.author}'
