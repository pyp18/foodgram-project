from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from recipes.forms import SignUpForm


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
    form = SignUpForm(request.POST) 
    print(form) 
    form = SignUpForm() 
    return render(request, 'signup.html', {'form': form}) 
