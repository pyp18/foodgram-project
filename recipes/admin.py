from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Tag, Favorite, Follow


class MembershipInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [MembershipInline]


# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)
admin.site.register(Tag)
admin.site.register(Favorite)
admin.site.register(Follow)
