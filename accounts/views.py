from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
from .forms import UserRegistrationForm, UserProfileForm, UserEditForm, UserProfileUpdateForm, PasswordChangeForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def user_list(request):
    users = User.objects.all().select_related('profile')
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query)
        )
    
    # Filter by role
    role_filter = request.GET.get('role', '')
    if role_filter:
        users = users.filter(profile__role=role_filter)
    
    # Pagination
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'users': page_obj,
        'search_query': search_query,
        'role_filter': role_filter,
    }
    return render(request, 'accounts/list.html', context)


@login_required
def user_edit(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('accounts:list')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileForm(instance=user.profile)
    return render(request, 'accounts/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_obj': user,
    })


@login_required
def user_delete(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        if user != request.user:
            user.delete()
            messages.success(request, 'User deleted successfully!')
        else:
            messages.error(request, 'You cannot delete your own account!')
        return redirect('accounts:list')
    return render(request, 'accounts/delete_confirm.html', {'user_obj': user})


@login_required
def profile_view(request):
    """View and edit current user's profile"""
    user = request.user
    # Ensure profile exists
    from .models import UserProfile
    profile, created = UserProfile.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            # Update user fields
            user.first_name = request.POST.get('first_name', '')
            user.last_name = request.POST.get('last_name', '')
            user.email = request.POST.get('email', '')
            user.save()
            
            # Update profile
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        profile_form = UserProfileUpdateForm(instance=profile)
        # Pre-populate user fields
        profile_form.fields['first_name'].initial = user.first_name
        profile_form.fields['last_name'].initial = user.last_name
        profile_form.fields['email'].initial = user.email
    
    return render(request, 'accounts/profile.html', {
        'profile_form': profile_form,
        'user': user,
        'profile': profile,
    })


@login_required
def change_password(request):
    """Change user password"""
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update session to prevent logout
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully!')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'accounts/change_password.html', {
        'form': form,
    })
