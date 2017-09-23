from django.db import models
from model_utils import Choices
from model_utils.fields import AutoCreatedField


class Klasifikasi(models.Model):
    jenis = models.CharField(max_length=255)


class Pengantar(models.Model):
    jenis = models.ForeignKey('arsip.Klasifikasi')
    nomor_surat = models.CharField(max_length=255)
    user = models.ForeignKey('users.User')
    KEPERLUAN = Choices(
        (1, 'pembuatan_ktp', 'Pembuatan KTP'),
        (2, 'perbaikan_data_ktp', 'Perbaikan Data KTP'),
        (3, 'pembuatan_skck', 'Pembuatan SKCK'),
        (4, 'keterangan_domisili', 'Domisili'),
        (5, 'keterangan_pindah', 'Keterangan Pindah'),
        (6, 'menikah', 'Menikah'),
        (7, 'cerai', 'Cerai'),
        (8, 'lainnya', 'Lainnya')
    )
    keperluan = models.PositiveSmallIntegerField(choices=KEPERLUAN)
    lainnya = models.TextField(blank=True)
    tanggal = AutoCreatedField()
