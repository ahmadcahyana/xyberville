from django.contrib import admin

from django.contrib.admin.forms import forms
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserAdditionForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserAdditionForm, self).__init__(*args, **kwargs)
        self.fields['type'] = forms.ChoiceField(choices=User.TYPE)


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None,
         {
            'fields': (
                'username',
                'name',
                'password',
                'email',
                'type',
                'permissions'
            )
         }
         ),
        ('Permissions',
         {'fields': (
             'is_active',
             'is_staff',
             'is_superuser'
         )
         }),
        ('Important dates', {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'type')
        }),
    )
    add_form = UserAdditionForm

    def mobile(self, obj):
        return obj.profile.mobile

    list_display = ('username', 'name', 'mobile', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active',)
    search_fields = ('username', 'name', 'profile__mobile')
    ordering = ('username',)


admin.site.register(User, UserAdmin)
