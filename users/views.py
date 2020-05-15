from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Blog


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account had been successfully created with username : {username} ! '
                                      f'Your are now able to login...')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_from = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_from.is_valid() and p_form.is_valid():
            u_from.save()
            p_form.save()
            messages.success(request, 'Your profile had been updated successfully!!!')
            return redirect('profile')
    else:
        u_from = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_from,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    blog = Blog.objects.filter(author=user)

    paginator = Paginator(blog, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'object': user,
        'page_obj': page_obj,
    }
    return render(request, 'user_profile.html', context)


# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, f'{username} already exists, Try with a different username')
#             elif User.objects.filter(email=email):
#                 messages.error(request, f'{email} is taken, Try with a different email')
#             else:
#                 user = User.objects.create_user(username=username, email=email, password=password1)
#                 user.save()
#                 messages.success(request, f'Your account had been created successfully!!!, You are now able to login')
#                 return redirect('login')
#         else:
#             messages.error(request, 'Your confirm password isn\'t matching with the password!!!')
#
#     return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!!!')
            return redirect('login')
    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('home')
