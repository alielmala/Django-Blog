from django.shortcuts import render, redirect
from django.contrib import messages
from djangoblog.views import home
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from djangoblog.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method =='POST':
        u_from = UserUpdateForm(request.POST, instance=request.user)
        p_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_from.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()
            messages.success(request, f'Your Account updated successfully')
            return redirect('profile')

    else:
        u_from = UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_from,
        'p_form':p_form
    }
    return render(request, 'users/profile.html', context)
