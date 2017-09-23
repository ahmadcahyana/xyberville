from django.db import models

from model_utils import Choices
from model_utils.fields import AutoCreatedField


class UserLogs(models.Model):
    user = models.ForeignKey(
        'users.User',
        related_name='user_logs'
    )
    user_edited = models.ForeignKey(
        'users.User',
        related_name='user_edited_logs'
    )
    ACTION = Choices(
        (1, 'created', 'Created'),
        (2, 'edited', 'Edited'),
    )
    action = models.PositiveIntegerField(choices=ACTION)
    created = AutoCreatedField()

    def __unicode__(self):
        return '#%s - User #%s' % (self.id, self.user_edited_id)


class KeluargaLogs(models.Model):
    user = models.ForeignKey(
        'users.User',
        related_name='keluarga_logs'
    )
    keluarga = models.ForeignKey(
        'keluarga.Keluarga',
        related_name='keluarga_logs'
    )
    ACTION = Choices(
        (1, 'created', 'Created'),
        (2, 'edited', 'Edited'),
    )
    action = models.PositiveIntegerField(choices=ACTION)
    created = AutoCreatedField()

    def __unicode__(self):
        return '#%s - Keluarga #%s' % (self.id, self.keluarga_id)


class UserProfileLogs(models.Model):
    user = models.ForeignKey(
        'users.User',
        related_name='profile_logs'
    )
    profile = models.ForeignKey(
        'profiles.Profile',
        related_name='profile_logs'
    )
    ACTION = Choices(
        (1, 'created', 'Created'),
        (2, 'edited', 'Edited'),
    )
    action = models.PositiveIntegerField(choices=ACTION)
    created = AutoCreatedField()

    def __unicode__(self):
        return '#%s - Profile #%s' % (self.id, self.profile_id)

