from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Recipe
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
from django.core.paginator import Paginator

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



class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('index') #  где login — это параметр "name" в path()
    template_name = "signupAndrew.html" 



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
    template_name = 'recipe_list.html'


class FavouriteView(LoginRequiredMixin, BaseRecipeListView):
    page_title = 'Recipes'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(favourites__user=self.request.user)

        return qs

def ProfileView(request, username):
    author = get_object_or_404(User, username=username)
    recipe = Recipe.objects.filter(
        user__username=username)
    paginator = Paginator(recipe, 10)
    favourites = author.favourites.filter(user=request.user.id)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(request, "recipe_list.html", {"page": page,
                                            "paginator": paginator,
                                            "user": author,
                                            "username": username,
                                            "favourites": favourites})
        