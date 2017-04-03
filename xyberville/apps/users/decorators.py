from functools import wraps

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


def super_user_required(view_func):
    def _check_user_account(request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        messages.error(request, "Anda tidak berhak mengakses halaman ini. "
                                "Silahkan Login terlebih dahulu.")
        return redirect(reverse('backoffice:login_view'))

    return wraps(view_func)(_check_user_account)


def staff_user_required(view_func):
    def _check_user_account(request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        messages.error(request, "Anda tidak berhak mengakses halaman ini. "
                                "Silahkan Login terlebih dahulu.")
        return redirect(reverse('backoffice:login_view'))

    return wraps(view_func)(_check_user_account)
