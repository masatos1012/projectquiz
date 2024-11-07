from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm, CustomAuthenticationForm


@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('quiz:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('quiz:index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('quiz:index')
    return render(request, 'account/logout.html')
