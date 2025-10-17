from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to "next" if present, else homepage
            next_url = request.POST.get('next') or 'shop_home'
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password")
    next_param = request.GET.get('next', '')
    return render(request, 'accounts/login.html', {'next': next_param})

# Logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('shop_home')
