from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from xyberville.apps.users.decorators import super_user_required


def login_view(request):
    auth_form = AuthenticationForm(data=request.POST or None)
    auth_form.fields['username'].widget.attrs = {
        'class': 'form-control',
        'id': 'username',
        'placeholder': 'Username'
    }
    auth_form.fields['password'].widget.attrs = {
        'class': 'form-control',
        'id': 'password',
        'placeholder': 'Password'
    }
    if auth_form.is_valid():
        login(request, auth_form.get_user())
        messages.success(request, 'Welcome to XyberVille Dashboard')
        return redirect('backoffice:index')
    else:
        invalid_data = request.method == 'POST'

    context_data = {
        'form': auth_form,
        'invalid_data': invalid_data,
        'title': 'Login'
    }
    return render(request, 'backoffice/login_view.html', context_data)


def logout_view(request):
    logout(request)
    return redirect('backoffice:login_view')


@super_user_required
def index(request):
    context_data = {
        'current_page': 'dashboard'
    }
    return render(request, 'backoffice/index.html', context_data)
