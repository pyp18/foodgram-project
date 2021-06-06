from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from recipes.forms import SignUpForm


def signup(request):
    form = SignUpForm(request.POST, files=request.FILES or None)
    if not form.is_valid():
        return render(request, 'registration/signup.html', {'form': form})
    form.save()
    username = form.cleaned_data.get('username')
    raw_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=raw_password)
    login(request, user)
    return redirect('index')
