from django.shortcuts import render, redirect
from . forms import UserCreationForm, RegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, "account created for" + user)
            return redirect('login')

    return render(request, 'registration.html', {'form': form, 'messages': messages})


def login(request):
    form=UserLoginForm
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                print('login was succesful and welcome to insta')
                return redirect('home')
            else:
                messages.info(request, "invalid credentials")
    return render(request, 'login.html', {'messages': messages,'form': form,})
