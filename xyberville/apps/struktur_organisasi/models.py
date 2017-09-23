from django.db import models


class RukunWarga(models.Model):
    rw = models.CharField(max_length=10)
    alamat_sekretariat = models.CharField(max_length=255)
    province = models.ForeignKey('regions.Province')
    regency = models.ForeignKey('regions.Regency')
    district = models.ForeignKey('regions.District')
    village = models.ForeignKey('regions.Village')
    kode_pos = models.CharField(max_length=255, blank=True)
    ketua = models.ForeignKey('users.User', blank=True, null=True, related_name='ketua_rw')
    wakil = models.ForeignKey('users.User', blank=True, null=True, related_name='wakil_rw')
    sekretaris = models.ForeignKey('users.User', blank=True, null=True, related_name='sekretaris_rw')
    bendahara = models.ForeignKey('users.User', blank=True, null=True, related_name='bendahara_rw')
    logo = models.ImageField(blank=True, null=True, upload_to='kop_surat')
    start_periods = models.DateField()
    end_periods = models.DateField()


class RukunTetanga(models.Model):
    rt = models.CharField(max_length=10)
    alamat_sekretariat = models.CharField(max_length=255)
    province = models.ForeignKey('regions.Province')
    regency = models.ForeignKey('regions.Regency')
    district = models.ForeignKey('regions.District')
    village = models.ForeignKey('regions.Village')
    kode_pos = models.CharField(max_length=255, blank=True)
    ketua = models.ForeignKey('users.User', blank=True, null=True, related_name='ketua_rt')
    wakil = models.ForeignKey('users.User', blank=True, null=True, related_name='wakil_rt')
    sekretaris = models.ForeignKey('users.User', blank=True, null=True, related_name='sekretaris_rt')
    bendahara = models.ForeignKey('users.User', blank=True, null=True, related_name='bendahara_rt')
    logo = models.ImageField(blank=True, null=True, upload_to='kop_surat')
    start_periods = models.DateField()
    end_periods = models.DateField()
