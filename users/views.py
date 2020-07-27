from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateFrom


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account for {username}!Login Now!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile)
        # print('***post')

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            print('updated****')
            messages.success(request, f'Your account has been updated!!')
            return redirect('profile')
            print('redirected****')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateFrom(instance=request.user.profile)

    return render(request, 'users/profile.html', {'u_form': u_form, 'p_form': p_form})
