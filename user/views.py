from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from recipes.forms import SignUpForm

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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
    return render(request, 'registration/signup.html', {'form': form}) 



def signup2(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup2.html', {'form': form})