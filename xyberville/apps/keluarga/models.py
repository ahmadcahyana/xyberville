from django.db import models
from xyberville.apps.users.models import User
from xyberville.apps.profiles.models import Profile


class Keluarga(models.Model):
    nomor_kk = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Nomor KK'
    )
    kepala_keluarga = models.ForeignKey(
        'users.User',
        related_name='family',
        verbose_name='Kepala Keluarga',
        blank=True,
        null=True
    )
    alamat = models.CharField(max_length=255)
    rt = models.CharField(max_length=255, blank=True)
    rw = models.CharField(max_length=255, blank=True)
    telepon = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    province = models.ForeignKey('regions.Province')
    regency = models.ForeignKey('regions.Regency')
    district = models.ForeignKey('regions.District')
    village = models.ForeignKey('regions.Village')

    def __unicode__(self):
        return self.nomor_kk

    @property
    def jumlah_keluarga(self):
        jumlah_keluarga = Profile.objects.filter(keluarga=self).count()
        return jumlah_keluarga

    def daftar_keluarga(self):
        users = Profile.objects.filter(keluarga=self).select_related('user')
        return users

    class Meta:
        verbose_name = 'keluarga'
        verbose_name_plural = 'keluargas'
        app_label = 'keluarga'
        db_table = 'keluarga'
