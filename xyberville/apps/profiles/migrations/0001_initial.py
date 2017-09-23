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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nik', models.CharField(blank=True, max_length=255)),
                ('alamat', models.CharField(blank=True, max_length=255)),
                ('rt', models.CharField(blank=True, max_length=255)),
                ('rw', models.CharField(blank=True, max_length=255)),
                ('kode_pos', models.CharField(blank=True, max_length=255)),
                ('kewarganegaraan', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'WNI (Warga Negera Indonesia)'), (2, 'WNA (Warga Negara Asing)')])),
                ('wna', models.CharField(blank=True, max_length=255)),
                ('paspor', models.CharField(blank=True, max_length=255)),
                ('paspor_kadaluarsa', models.DateField(blank=True, null=True)),
                ('kelamin', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Laki-laki'), (2, 'Perempuan')])),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('nomor_akta_lahir', models.CharField(blank=True, max_length=255)),
                ('tanggal_akta_lahir', models.DateField(blank=True, null=True)),
                ('golongan_darah', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'A'), (2, 'B'), (3, 'AB'), (4, 'O'), (5, 'A+'), (6, 'B+'), (7, 'AB+'), (8, 'O+'), (9, 'A-'), (10, 'B-'), (11, 'AB-'), (12, 'O-')])),
                ('agama', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Islam'), (2, 'Kristen'), (3, 'Katolik'), (4, 'Hindu'), (5, 'Buddha'), (6, 'Lainnya')])),
                ('status_pernikahan', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Lajang'), (2, 'Menikah'), (3, 'Cerai'), (4, 'Cerai Mati')])),
                ('nomor_akta_nikah', models.CharField(blank=True, max_length=255)),
                ('tanggal_pernikahan', models.DateField(blank=True, null=True)),
                ('nomor_akta_cerai', models.CharField(blank=True, max_length=255)),
                ('tanggal_perceraian', models.DateField(blank=True, null=True)),
                ('hubungan_keluarga', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Kepala Keluarga'), (2, 'Suami'), (3, 'Istri'), (4, 'Anak'), (5, 'Menantu'), (6, 'Cucu'), (7, 'Orang Tua'), (8, 'Mertua'), (9, 'Famili Lain'), (10, 'Pembantu'), (11, 'Lainnya')])),
                ('penyandang_cacat', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Tidak'), (2, 'Cacat Fisik'), (3, 'Tunanetra'), (4, 'Tunarungu'), (5, 'Cacat Mental'), (6, 'Cacat Fisik dan Mental'), (7, 'Lainnya')])),
                ('pendidikan', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Tidak/Belum Sekolah'), (2, 'Belum Tamat SD'), (3, 'SD'), (4, 'SLTP/Sederajat'), (5, 'SLTA/Sederajat'), (6, 'Diploma I/II'), (7, 'Diploma III / Sarjana Muda'), (8, 'Strata I (S1)'), (9, 'Strata II (S2)'), (10, 'Strata III (S3)')])),
                ('telepon', models.CharField(blank=True, max_length=30)),
                ('mobile', models.CharField(blank=True, max_length=30)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='avatar')),
                ('status_penduduk', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Tetap'), (2, 'Tidak Tetap')])),
                ('status_tempat_tinggal', models.PositiveSmallIntegerField(blank=True, null=True, choices=[(1, 'Pemilik'), (2, 'Keluarga'), (3, 'Sewa')])),
            ],
        ),
    ]
