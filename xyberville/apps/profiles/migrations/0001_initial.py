# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nik', models.CharField(max_length=255, blank=True)),
                ('alamat', models.CharField(max_length=255, blank=True)),
                ('rt', models.CharField(max_length=255, blank=True)),
                ('rw', models.CharField(max_length=255, blank=True)),
                ('kode_pos', models.CharField(max_length=255, blank=True)),
                ('kewarganegaraan', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'WNI (Warga Negera Indonesia)'), (2, b'WNA (Warga Negara Asing)')])),
                ('wna', models.CharField(max_length=255, blank=True)),
                ('paspor', models.CharField(max_length=255, blank=True)),
                ('paspor_kadaluarsa', models.DateField(null=True, blank=True)),
                ('kelamin', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Laki-laki'), (2, b'Perempuan')])),
                ('tanggal_lahir', models.DateField(null=True, blank=True)),
                ('nomor_akta_lahir', models.CharField(max_length=255, blank=True)),
                ('tanggal_akta_lahir', models.DateField(null=True, blank=True)),
                ('golongan_darah', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'A'), (2, b'B'), (3, b'AB'), (4, b'O'), (5, b'A+'), (6, b'B+'), (7, b'AB+'), (8, b'O+'), (9, b'A-'), (10, b'B-'), (11, b'AB-'), (12, b'O-')])),
                ('agama', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Islam'), (2, b'Kristen'), (3, b'Katolik'), (4, b'Hindu'), (5, b'Buddha'), (6, b'Lainnya')])),
                ('status_pernikahan', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Lajang'), (2, b'Menikah'), (3, b'Cerai'), (4, b'Cerai Mati')])),
                ('nomor_akta_nikah', models.CharField(max_length=255, blank=True)),
                ('tanggal_pernikahan', models.DateField(null=True, blank=True)),
                ('nomor_akta_cerai', models.CharField(max_length=255, blank=True)),
                ('tanggal_perceraian', models.DateField(null=True, blank=True)),
                ('hubungan_keluarga', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Kepala Keluarga'), (2, b'Suami'), (3, b'Istri'), (4, b'Anak'), (5, b'Menantu'), (6, b'Cucu'), (7, b'Orang Tua'), (8, b'Mertua'), (9, b'Famili Lain'), (10, b'Pembantu'), (11, b'Lainnya')])),
                ('penyandang_cacat', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Cacat Fisik'), (2, b'Tunanetra'), (3, b'Tunarungu'), (4, b'Cacat Mental'), (5, b'Cacat Fisik dan Mental'), (6, b'Lainnya')])),
                ('pendidikan', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Tidak/Belum Sekolah'), (2, b'Belum Tamat SD'), (3, b'SD'), (4, b'SLTP/Sederajat'), (5, b'SLTA/Sederajat'), (6, b'Diploma I/II'), (7, b'Diploma III / Sarjana Muda'), (8, b'Strata I (S1)'), (9, b'Strata II (S2)'), (10, b'Strata III (S3)')])),
                ('telepon', models.CharField(max_length=30, blank=True)),
                ('mobile', models.CharField(max_length=30, blank=True)),
                ('photo', models.ImageField(null=True, upload_to=b'uploaded_images', blank=True)),
                ('status_penduduk', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Tetap'), (2, b'Tidak Tetap')])),
                ('status_tempat_tinggal', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, b'Pemilik'), (2, b'Keluarga'), (3, b'Sewa')])),
            ],
        ),
    ]
