from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Favourite, Recipe
from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
from django.contrib.auth.decorators import login_required 
from recipes.forms import RecipeForm
from django.shortcuts import redirect 
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

User = get_user_model()

@login_required 
def new_recipe(request): 
    form = RecipeForm(request.POST or None, files=request.FILES or None) 
    if not form.is_valid():
        a_file = open("test.txt", "w")
        text = form
        print(text, file=a_file)
        a_file.close()
        return render(request, 'formRecipe.html', {'form': form, 'is_new': True}) 
    recipe = form.save(commit=False)
    recipe.user = request.user
    a_file = open("test.txt", "w")
    text = form
    print(text, file=a_file)
    a_file.close()
    print("SAVED")
    return redirect('index')


def add_to_favorite(request):
    Favourite.objects.get_or_create(user=request.user, recipe=request.recipe.id)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm(request.POST)
        print(form)
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



class BaseRecipeListView(ListView):
    context_object_name = 'recipe_list'
    queryset = Recipe.objects.all()
    paginate_by = 6
    page_title = None

    def get_context_data(self, **kwargs):
        kwargs.update({'page_title':self.get_page_title()})

        return super().get_context_data(**kwargs)

    def get_page_title(self):
        assert self.page_title, f'Attribute "page_title" is not set for {self.__class__.__name__}'

        return self.page_title


class IndexView(BaseRecipeListView):
    page_title = 'Recipes'
    template_name = 'ready/recipe_list.html'


class FavouriteView(LoginRequiredMixin, BaseRecipeListView):
    page_title = 'Избранное'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        qs = qs.filter(favourites__user=self.request.user).with_is_favorite(user_id=user.id)

        return qs

class ProfileView(BaseRecipeListView):

    template_name = 'ready/profile.html'

    def get(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, username=kwargs.get('username'))

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.user).with_is_favorite(user_id=self.user.id)

        return qs

    def get_page_title(self):
        return self.user.get_full_name()
        

class RecipeDetailView(DetailView):
    queryset = Recipe.objects.all()
    template_name = 'RecipePage.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.with_is_favorite(user_id=self.request.user.id)

        return qs
