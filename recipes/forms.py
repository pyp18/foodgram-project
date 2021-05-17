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



from django import forms 
 
 
class RecipeForm(ModelForm): 
    class Meta: 
        # ru на основе какой модели создаётся класс формы 
        model = Recipe
        # ru укажем, какие поля будут в форме 
        fields = ('title', 'tag', 'ingredient', 'time_cooking', 'text', 'image') 
 
    def clean_text(self): 
        data = self.cleaned_data['text'] 
        if not data: 
            raise forms.ValidationError('Напишите хоть что нибудь!') 
        return data 