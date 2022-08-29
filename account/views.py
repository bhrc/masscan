from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from contents.models import Content, Author, Category, Tag, Geotag, Publication
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user-change-pass.html'
    success_message = "پسورد شما با موفقیت تغییر کرد."
    success_url = '/account/login'


@login_required
def update(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('/account')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'user-update.html', {'user_form': user_form})


def index(request):
    if request.user.is_authenticated:
        contents = Content.objects.filter(created_by= request.user.username)
        if request.user.is_staff:
            contents_drafts = Content.objects.filter(published=False)
            return render(request, 'account.html', {'cases': contents, 'case_drafts': contents_drafts})
        else:
            return render(request, 'account.html', {'cases': contents})
    else:
        return redirect('/account/login')


def register(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'user already exist')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    print('user created successfully.')
                    return redirect('login')
            else:
                messages.info(request, 'Passwords are not matched. The user is not created')
                return redirect('register')
                print('Passwords are not matched')
            return redirect('/account')
        else:
            return render(request, 'register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/account')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/account')
            else:
                messages.info(request, 'invalid credintials')
                return redirect('login')
        else:
            return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')