from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from home.models import Property

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(f"Login attempt: {username} / {password}")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")
        if user is not None:
            auth_login(request, user)
            return redirect('proUI')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    return render(request, 'login.html')


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('proUI')  # Redirect normal users to proUI.html
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirmPassword')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'signup.html')

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'signup.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('/login')

def proUI_view(request):
    return render(request, 'proUI.html')

