from django.shortcuts import render, redirect
from . forms import UserCreationForm, RegisterForm
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.method =="POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request, "account created for" + user )
                return redirect('login')

    return render(request, 'registration.html', {'form': form})
