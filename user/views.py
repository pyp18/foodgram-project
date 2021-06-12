from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def signup2(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup2.html', {'form': form})