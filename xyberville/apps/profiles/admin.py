from django.contrib import admin
from dal import autocomplete

from .models import Profile


admin.site.register(Profile)
