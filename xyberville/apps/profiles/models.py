from django.db import models
from model_utils import Choices
from xyberville.apps.users.models import User
import datetime


class Profile(models.Model):
    user = models.OneToOneField(
        'users.User',
        verbose_name='User'
    )
    nik = models.CharField(
        max_length=255,
        blank=True
    )
    alamat = models.CharField(
        max_length=255,
        blank=True
    )
    rt = models.CharField(
        max_length=255,
        blank=True
    )
    rw = models.CharField(
        max_length=255,
        blank=True
    )
    province = models.ForeignKey('regions.Province')
    regency = models.ForeignKey('regions.Regency')
    district = models.ForeignKey('regions.District')
    village = models.ForeignKey('regions.Village')
    kode_pos = models.CharField(
        max_length=255,
        blank=True
    )
    WNI = Choices(
        (1, 'wni', 'WNI (Warga Negera Indonesia)'),
        (2, 'wna', 'WNA (Warga Negara Asing)')
    )
    kewarganegaraan = models.PositiveSmallIntegerField(
        choices=WNI,
        blank=True,
        null=True
    )
    wna = models.CharField(
        max_length=255,
        blank=True
    )
    paspor = models.CharField(
        max_length=255,
        blank=True
    )
    paspor_kadaluarsa = models.DateField(
        blank=True,
        null=True
    )
    KELAMIN = Choices(
        (1, 'laki', 'Laki-laki'),
        (2, 'perempuan', 'Perempuan'),
    )
    kelamin = models.PositiveSmallIntegerField(
        choices=KELAMIN,
        blank=True,
        null=True
    )
    tempat_lahir = models.ForeignKey(
        'regions.Regency',
        related_name='tempat_lahir',
        blank=True,
        null=True,
    )
    tanggal_lahir = models.DateField(
        blank=True,
        null=True
    )
    nomor_akta_lahir = models.CharField(
        max_length=255,
        blank=True
    )
    tanggal_akta_lahir = models.DateField(
        blank=True,
        null=True
    )
    GOLONGAN_DARAH = Choices(
        (1, 'a', 'A'),
        (2, 'b', 'B'),
        (3, 'ab', 'AB'),
        (4, 'o', 'O'),
        (5, 'a+', 'A+'),
        (6, 'b+', 'B+'),
        (7, 'ab+', 'AB+'),
        (8, 'o+', 'O+'),
        (9, 'a-', 'A-'),
        (10, 'b-', 'B-'),
        (11, 'ab-', 'AB-'),
        (12, 'o-', 'O-')
    )
    golongan_darah = models.PositiveSmallIntegerField(
        choices=GOLONGAN_DARAH,
        blank=True,
        null=True
    )
    AGAMA = Choices(
        (1, 'islam', 'Islam'),
        (2, 'kristen', 'Kristen'),
        (3, 'katolik', 'Katolik'),
        (4, 'hindu', 'Hindu'),
        (5, 'buddha', 'Buddha'),
        (6, 'lainnya', 'Lainnya')
    )
    agama = models.PositiveSmallIntegerField(
        choices=AGAMA,
        blank=True,
        null=True
    )
    STATUS_PERNIKAHAN = Choices(
        (1, 'lajang', 'Lajang'),
        (2, 'menikah', 'Menikah'),
        (3, 'cerai', 'Cerai'),
        (4, 'cerai_mati', 'Cerai Mati')
    )
    status_pernikahan = models.PositiveSmallIntegerField(
        choices=STATUS_PERNIKAHAN,
        blank=True,
        null=True
    )
    nomor_akta_nikah = models.CharField(
        max_length=255,
        blank=True
    )
    tanggal_pernikahan = models.DateField(
        blank=True,
        null=True
    )
    nomor_akta_cerai = models.CharField(
        max_length=255,
        blank=True
    )
    tanggal_perceraian = models.DateField(
        blank=True,
        null=True
    )
    HUBUNGAN_KELUARGA = Choices(
        (1, 'kepala_keluarga', 'Kepala Keluarga'),
        (2, 'suami', 'Suami'),
        (3, 'istri', 'Istri'),
        (4, 'anak', 'Anak'),
        (5, 'menantu', 'Menantu'),
        (6, 'cucu', 'Cucu'),
        (7, 'orang_tua', 'Orang Tua'),
        (8, 'mertua', 'Mertua'),
        (9, 'famili_lain', 'Famili Lain'),
        (10, 'pembantu', 'Pembantu'),
        (11, 'lainnya', 'Lainnya')
    )
    hubungan_keluarga = models.PositiveSmallIntegerField(
        choices=HUBUNGAN_KELUARGA,
        blank=True,
        null=True
    )
    CACAT = Choices(
        (1, 'tidak', 'Tidak'),
        (2, 'cacat_fisik', 'Cacat Fisik'),
        (3, 'tuna_netra', 'Tunanetra'),
        (4, 'tuna_rungu', 'Tunarungu'),
        (5, 'cacat_mental', 'Cacat Mental'),
        (6, 'cacat_fisik_dan_mental', 'Cacat Fisik dan Mental'),
        (7, 'lainnya', 'Lainnya')
    )
    penyandang_cacat = models.PositiveSmallIntegerField(
        choices=CACAT,
        blank=True,
        null=True
    )
    ibu = models.ForeignKey(
        'users.User',
        related_name='ibu',
        blank=True,
        null=True)
    ayah = models.ForeignKey(
        'users.User',
        related_name='ayah',
        blank=True,
        null=True)
    PENDIDIKAN = Choices(
        (1, 'tidak', 'Tidak/Belum Sekolah'),
        (2, 'belum_tamat_sd', 'Belum Tamat SD'),
        (3, 'sd', 'SD'),
        (4, 'sltp', 'SLTP/Sederajat'),
        (5, 'slta', 'SLTA/Sederajat'),
        (6, 'diploma_i_atau_ii', 'Diploma I/II'),
        (7, 'diploma_iii', 'Diploma III / Sarjana Muda'),
        (8, 'strata_1', 'Strata I (S1)'),
        (9, 'strata_2', 'Strata II (S2)'),
        (10, 'strata_3', 'Strata III (S3)')
    )
    pendidikan = models.PositiveSmallIntegerField(
        choices=PENDIDIKAN, blank=True, null=True
    )
    pekerjaan = models.ForeignKey(
        'pekerjaan.Pekerjaan',
        related_name='pekerjaan',
        blank=True,
        null=True
    )
    telepon = models.CharField(
        max_length=30,
        blank=True
    )
    mobile = models.CharField(
        max_length=30,
        blank=True
    )
    keluarga = models.ForeignKey(
        'keluarga.Keluarga',
        related_name='keluarga',
        blank=True,
        null=True
    )
    photo = models.ImageField(
        blank=True, null=True, upload_to='avatar'
    )
    STATUS_PENDUDUK = Choices(
        (1, 'tetap', 'Tetap'),
        (2, 'tidak_tetap', 'Tidak Tetap')
    )
    status_penduduk = models.PositiveSmallIntegerField(
        choices=STATUS_PENDUDUK,
        blank=True,
        null=True
    )
    STATUS_TEMPAT_TINGGAL = Choices(
        (1, 'pemilik', 'Pemilik'),
        (2, 'keluarga', 'Keluarga'),
        (3, 'sewa', 'Sewa')
    )
    status_tempat_tinggal = models.PositiveSmallIntegerField(
        choices=STATUS_TEMPAT_TINGGAL,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.user.name

    @property
    def age(self):
        on = datetime.date.today()
        was_earlier = (on.month, on.day) < (self.tanggal_lahir.month,
                                            self.tanggal_lahir.day)
        return on.year - self.tanggal_lahir.year - (was_earlier)

