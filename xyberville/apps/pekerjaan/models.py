from django.db import models


class Pekerjaan(models.Model):
    nama = models.CharField(max_length=255)
    keterangan = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.nama
