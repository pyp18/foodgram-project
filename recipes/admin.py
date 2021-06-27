from django.contrib import admin
from .models import (Ingredient, Recipe, RecipeIngredient,
                     Tag, Favorite, Follow, ShoppingList)
from django import forms


class MembershipInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = ((MembershipInline),)
    list_display = ('title', 'user', 'pub_date', 'time_cooking',)
    list_filter = ('tags',)
    search_fields = ['user__username', 'title', 'text', 'user__email' ]
    date_hierarchy = 'publish'

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit')
    list_filter = ('unit',)
    search_fields = ['title', 'unit', ]


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ['user__username', 'recipe__text', 'recipe__title']


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author')
    search_fields = ['user__username', 'author__username', 'user__email']


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')
    search_fields = ['user__username', 'recipe__title', 'recipe__text', 'user__email']



admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Tag)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)
