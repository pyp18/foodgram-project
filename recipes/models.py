from typing import Optional
from django.db import models
from django import forms
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Exists
from django.db.models import OuterRef, Exists
from django.core.exceptions import ValidationError


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
        max_length=50, verbose_name='Цвет тега', default='Red')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

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
        return f'{self.title}, {self.unit}'


class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipes', verbose_name='Автор')
    title = models.CharField(max_length=150, verbose_name='Название рецепта')
    image = models.ImageField(
        upload_to='images/',verbose_name='Картинка')
    text = models.TextField(verbose_name='Описание')
    tags = models.ManyToManyField(Tag, related_name='tags', verbose_name='Тэги')
    time_cooking = models.PositiveIntegerField(verbose_name='Время готовки')
    slug = models.SlugField(max_length=40, unique=False, verbose_name='Слаг')
    ingredient = models.ManyToManyField(
        Ingredient, through='RecipeIngredient', related_name='ingredients', verbose_name='Игредиенты')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    objects = RecipeQuerySet.as_manager()


    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='recipe_ingredient')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Ингридиент рецепта'
        verbose_name_plural = 'Ингридиенты рецепта'

    def __str__(self):
        return f'{self.ingredient}, {self.recipe}'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='favorites', verbose_name='пользователь')
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='favorites', verbose_name='рецепт')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f'Избранный {self.recipe} у {self.user}'


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='self_follow'
            ),
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_author'
            )
        ]


    def __str__(self):
        return f'{self.user} на {self.author}'


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='buyer',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Рецепт'
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'


    def __str__(self):
        return f'{self.user} на {self.recipe}'
