from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CustomUserCreationForm, ProfileUpdateForm

User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('feed')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'core/profile.html', {'user': user})


@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'core/edit_profile.html', {'form': form})


@login_required
def worker_panel(request):
    return render(request, 'core/worker_panels.html')


@login_required
def admin_panel(request):
    return render(request, 'core/admin_panel.html')
