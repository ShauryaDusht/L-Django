from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

# we use inbuilt forms for authentication in django

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} is currently logged in')
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
@login_required
def profile(request):
    return render(request, 'users/profile.html')