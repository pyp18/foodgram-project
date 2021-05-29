from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Favorite, Recipe, RecipeIngredient, Ingredient, Follow, ShoppingList
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from recipes.forms import RecipeForm
from django.shortcuts import redirect
from foodgram.settings import GlobalPaginator


User = get_user_model()


def get_ingredients(request):
    ingredients = {}
    for key in request.POST:
        if key.startswith('nameIngredient'):
            value_ingredient = key[15:]
            ingredients[request.POST[key]] = request.POST[
                'valueIngredient_' + value_ingredient
            ]
    return ingredients


def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    ingredients = get_ingredients(request)
    if not form.is_valid():
        return render(request, 'formRecipe.html', {
            'form': form,
            'is_new': True,
        },
        )
    recipe = form.save(commit=False)
    recipe.user = request.user
    recipe.save()
    RecipeIngredient.objects.filter(recipe=recipe).delete()
    objs = []
    for title, count in ingredients.items():
        ingredient = get_object_or_404(Ingredient, title=title)
        objs.append(RecipeIngredient(
            recipe=recipe,
            ingredient=ingredient,
            count=count
        )
        )
    RecipeIngredient.objects.bulk_create(objs)
    form.save_m2m()
    return redirect('index')


def recipe_edit(request, id):
    recipe_base = get_object_or_404(Recipe, pk=id)
    form = RecipeForm(request.POST or None,
                      files=request.FILES or None, instance=recipe_base)
    ingredients = get_ingredients(request)
    if not form.is_valid():
        return render(request, 'EditRecipe.html', {
            'form': form,
            'is_new': True,
            'recipe': recipe_base
        },
        )
    recipe = form.save(commit=False)
    recipe.user = request.user
    recipe.save()
    RecipeIngredient.objects.filter(recipe=recipe).delete()
    objs = []
    for title, count in ingredients.items():
        ingredient = get_object_or_404(Ingredient, title=title)
        objs.append(RecipeIngredient(
            recipe=recipe,
            ingredient=ingredient,
            count=count
        )
        )
    RecipeIngredient.objects.bulk_create(objs)
    form.save_m2m()
    return redirect('index')


def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, user=request.user, id=id)
    recipe.delete()
    return redirect('index')


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    following = author.following.exists()
    if request.user != author and not following:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('profile', username=username)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    get_object_or_404(Follow, user=request.user, author=author).delete()
    return redirect('profile', username=username)


@login_required
def profile_follow_recipe_page(request, pk, username):
    author = get_object_or_404(User, username=username)
    following = author.following.exists()
    if request.user != author and not following:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('recipe', pk=pk)


@login_required
def profile_unfollow_recipe_page(request, pk, username):
    author = get_object_or_404(User, username=username)
    get_object_or_404(Follow, user=request.user, author=author).delete()
    return redirect('recipe', pk=pk)


class BaseRecipeListView(ListView):
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.all()
    paginate_by = GlobalPaginator
    page_title = None

    def get_context_data(self, **kwargs):
        kwargs.update({'page_title': self.get_page_title()})

        return super().get_context_data(**kwargs)

    def get_page_title(self):
        return self.page_title


class IndexView(BaseRecipeListView):
    page_title = 'Recipes'
    template_name = 'recipe_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        qs = qs.with_is_favorite(user_id=user.id)

        return qs


class FavouriteView(LoginRequiredMixin, BaseRecipeListView):
    page_title = 'Избранное'
    template_name = 'recipe_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        qs = qs.filter(favorites__user=self.request.user).with_is_favorite(
            user_id=user.id)

        return qs


class SubscriptionsView(LoginRequiredMixin, BaseRecipeListView):
    page_title = 'Подписки'
    template_name = 'myFollow.html'

    def get_queryset(self):
        qs = Follow.objects.all()
        user = self.request.user
        qs = qs.filter(user=user)

        return qs


def profile(request, username):
    author = get_object_or_404(User, username=username)
    page_obj = author.recipes.all()
    following = author.following.exists()
    context = {
        'author': author,
        'following': following,
        'page_obj': page_obj,
        'user': username
    }
    return render(request, 'profile_list.html', context)


class RecipeDetailView(DetailView):
    queryset = Recipe.objects.all()
    template_name = 'RecipePage.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.with_is_favorite(user_id=self.request.user.id)

        return qs


@login_required
def shopping_list(request):
    shopping_list = ShoppingList.objects.filter(user=request.user).all()
    return render(
        request,
        'shopping_list.html',
        {'shopping_list': shopping_list},
    )


@login_required
def shopping_list_download(request):
    result = shopping_list_ingredients(request)
    response = HttpResponse(result, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename = download.txt'
    return response


@login_required
def shopping_list_ingredients(request):
    shopping_list = ShoppingList.objects.filter(user=request.user).all()
    ingredients = {}
    for item in shopping_list:
        for x in item.recipe.recipe_ingredient.all():
            name = f'{x.ingredient.title} ({x.ingredient.unit})'
            units = x.count
            if name in ingredients.keys():
                ingredients[name] += units
            else:
                ingredients[name] = units
    download = []
    for key, units in ingredients.items():
        download.append(f'{key} - {units} \n')
    return download
