from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import Group
from .models import CustomUser


# Create your views here.
def login(request):
    try:
        if request.method != 'POST':
            return render(request, 'accounts/login.html')
        else:
            #  collect User information
            loginusername = request.POST['username']
            loginpassword = request.POST['password']

            # validating user information
            user = auth.authenticate(username=loginusername, password=loginpassword)

            # saving user information
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect('dashboard')
            else:
                messages.error(request, "Username or Password is not matched. Please try again !")
                return redirect(request.META['HTTP_REFERER'])
    except:
        return redirect('index')


def register(request):
    if request.method == 'POST':
        # Get form values
        group_check = int(request.POST['group'])
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request,'The username is already taken')
                return redirect('register')
            else:
            # Check email
                if CustomUser.objects.filter(email=email).exists():
                    messages.error(request,'The email is already taken')
                    return redirect('register')
                else:
                    #Looks good
                    user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    if group_check == 2:
                        group = Group.objects.get(name='Home_owner')
                    else:
                        group = Group.objects.get(name='user')
                    
                    user.groups.add(group)
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('accounts/register.html')
    else:
        return render(request,'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')