from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from members.models import Member
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def register(request):
    if request.method == 'POST':
        # Get form values
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        display_name = request.POST['display_name']
        branch = request.POST['branch']
        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                # Store user detals
                user = User.objects.create_user(username=username, password=password, email=email)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                member = Member(user=user, display_name=display_name, branch=branch, email=email)
                member.save()
                send_mail(
                    'GECT Alumni New Account Registered - ' + display_name,
                    'New account with name: ' + display_name + ', email: ' + email + ', branch: ' + branch + ' username: ' + username + ' regsitered with GECT Alumni. Login to authorize access ',
                    'tebby.thomas@gmail.com',
                    #[email, 'tebby.thomas@gmail.com'],
                    ['tebby.thomas@gmail.com'],
                    fail_silently=False
                )
                messages.success(request, 'You are now registered and can login')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # Login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
    return


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

def change_username(request):
    if request.method == 'POST':
        new_username = request.POST['new-username']
        curr_username = request.POST['curr-username']
        if User.objects.filter(username=new_username).exists():
            messages.error(request, 'That username is taken')
            return redirect('change_username')
        user = User.objects.get(username = curr_username)
        user.username = new_username
        user.save()
        messages.success(request, 'Your username was successfully updated!')
        return redirect('index')
    else:
        return render(request, 'accounts/change-username.html')