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
            if ' ' in username:
                messages.error(request, 'Username cannot have spaces')
                return redirect('register')
            if User.objects.filter(username__iexact=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            elif User.objects.filter(email__iexact=email).exists():
                messages.error(request, 'That email is being used')
                return redirect('register')
            else:
                # Store user detals
                email = email.lower()
                user = User.objects.create_user(username=username, password=password, email=email)
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                member = Member(user=user, display_name=display_name, branch=branch, email=email)
                member.save()
                to_list = ['tomy.thomas@gmail.com', email]
                if branch == 'chemical':
                    to_list.append('profmadhugopal@gmail.com')
                elif branch =='civil':
                    to_list.append('hardahari@yahoo.co.in')
                elif branch == 'electrical':
                    to_list.append('drpai1962@yahoo.com')
                    to_list.append('sreekumarbkartha@gmail.com')
                elif branch =='mechanical':
                    to_list.append('drpai62@gmail.com')
                    to_list.append('antojoyp@gmail.com')
                elif branch =='production':
                    to_list.append('avittom@gmail.com')
                
                # send_mail(
                #     'GECT Alumni 1984 - New Account Registered : ' + display_name,
                #     'Hello Administrator,\n\nNew account registered on the GECT Alumni 1984 website (https://tec84.in) with the following details:\n\nName: ' + display_name + '\nEmail: ' + email + '\nBranch: ' + branch + '\nUsername: ' + username + '\n\nYou may login at the following link to authorize access:\nhttps://tec84.in/admin \n\nThanks and Regards,\nGECT-Alumni 1984 Team',
                #     'tomy.thomas@gmail.com',
                #     to_list,
                #     fail_silently=True
                # )

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