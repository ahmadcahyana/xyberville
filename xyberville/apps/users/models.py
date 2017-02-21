from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.utils import timezone
from model_utils import Choices


class CustomUserManager(UserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        now = timezone.now()
        user = self.model(
            username=username,
            is_staff=False,
            is_active=True,
            is_superuser=False,
            last_login=now,
            date_joined=now,
            **extra_fields
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=255,
        blank=True,
        unique=True,
        db_index=True
    )
    # Name, email and mobile needs to be case insensitive indexed in postgres
    email = models.EmailField(
        null=True,
        blank=True,
        max_length=255,
    )
    name = models.CharField(
        max_length=255,
        blank=True
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False
    )
    is_active = models.BooleanField(
        'active',
        default=True
    )
    date_joined = models.DateTimeField(
        'date joined',
        default=timezone.now
    )
    TYPE = Choices(
        (1, 'ketua_rw', 'Ketua RW'),
        (2, 'wakil_ketua_rw', 'Wakil Ketua RW'),
        (3, 'sekretaris', 'Sekretaris'),
        (4, 'bendahara', 'Bendahara'),
        (5, 'ketua_rt', 'Ketua RT')
    )
    type = models.PositiveSmallIntegerField(
        choices=TYPE,
        blank=True,
        null=True
    )
    permissions = models.ManyToManyField(
        'permissions.Permission',
        related_name='permissions'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.name

    def get_label(self):
        label = self.name + ' (' + self.profile.nik + ')'
        return label
