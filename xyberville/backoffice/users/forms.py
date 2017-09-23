from django import forms
from model_utils import Choices
from xyberville.apps.users.models import User
from xyberville.apps.keluarga.models import Keluarga
from xyberville.apps.profiles.models import Profile
from xyberville.apps.pekerjaan.models import Pekerjaan
from xyberville.core.utils import (generate_random_string, generate_username)
from xyberville.apps.logs.models import UserLogs
from xyberville.apps.regions.models import Province, Regency, District, Village
from dal import autocomplete, forward


class BaseUserForm(forms.ModelForm):
    name = forms.CharField(
        label='Nama',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nama Lengkap'
            }
        )
    )
    nik = forms.CharField(
        required=False,
        label='NIK',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'NIK'
            }
        )
    )
    alamat = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Alamat'
            }
        )
    )
    rt = forms.CharField(
        required=False,
        label='RT',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'RT'
            }
        )
    )
    rw = forms.CharField(
        required=False,
        label='RW',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'RW'
            }
        )
    )
    province = forms.ModelChoiceField(
        label='Provinsi',
        queryset=Province.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:province_autocomplete')
    )
    regency = forms.ModelChoiceField(
        label='Kabupaten / Kota',
        queryset=Regency.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:regency_autocomplete',
            forward=(forward.Field('province', 'province'),)
        )
    )
    district = forms.ModelChoiceField(
        label='Kecamatan',
        queryset=District.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:district_autocomplete',
            forward=(forward.Field('regency', 'regency'),)
        )
    )
    village = forms.ModelChoiceField(
        label='Kelurahan',
        queryset=Village.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:village_autocomplete',
            forward=(forward.Field('district', 'district'),)
        )
    )
    kode_pos = forms.CharField(
        required=False,
        label='Kode Pos',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Kode Pos'
            }
        )
    )
    kewarganegaraan = forms.ChoiceField(
        required=False,
        choices=Profile.WNI,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    wna = forms.CharField(
        required=False,
        label='WNA',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Negara Asal'
            }
        )
    )
    paspor = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Paspor'
            }
        )
    )
    paspor_kadaluarsa = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'paspor_kadaluarsa',
                'placeholder': 'YYYY/MM/DD'
            }
        )
    )
    status_penduduk = forms.ChoiceField(
        required=False,
        label='Penduduk Tetap',
        choices=Profile.STATUS_PENDUDUK,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    status_tempat_tinggal = forms.ChoiceField(
        required=False,
        label='Status Tempat Tinggal',
        choices=Profile.STATUS_TEMPAT_TINGGAL,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    kelamin = forms.ChoiceField(
        required=False,
        choices=Profile.KELAMIN,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    tempat_lahir = forms.ModelChoiceField(
        label='Tempat Lahir',
        queryset=Regency.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:regency_autocomplete'
        )
    )
    tanggal_lahir = forms.DateField(
        required=False,
        label='Tanggal Lahir',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tanggal_lahir',
                'data-date-format': 'yyyy-mm-dd'
            }
        )
    )
    nomor_akta_lahir = forms.CharField(
        required=False,
        label='No. Akta Lahir',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nomor Akta Lahir'
            }
        )
    )
    golongan_darah = forms.ChoiceField(
        required=False,
        label='Gol. Darah',
        choices=Profile.GOLONGAN_DARAH,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    agama = forms.ChoiceField(
        required=False,
        choices=Profile.AGAMA,
        label='Agama',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    status_pernikahan = forms.ChoiceField(
        required=False,
        label='Status Pernikahan',
        choices=Profile.STATUS_PERNIKAHAN,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    nomor_akta_nikah = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nomor Akta Nikah'
            }
        )
    )
    tanggal_pernikahan = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tanggal_pernikahan',
                'placeholder': 'YYYY-MM-DD',
                'data-date-format': 'yyyy-mm-dd'
            }
        )
    )
    nomor_akta_cerai = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nomor Akta Cerai'
            }
        )
    )
    tanggal_perceraian = forms.DateField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'tanggal_perceraian',
                'placeholder': 'YYYY-MM-DD',
                'data-date-format': 'yyyy-mm-dd'
            }
        )
    )
    hubungan_keluarga = forms.ChoiceField(
        required=False,
        choices=Profile.HUBUNGAN_KELUARGA,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    penyandang_cacat = forms.ChoiceField(
        required=False,
        choices=Profile.CACAT,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    pendidikan = forms.ChoiceField(
        required=False,
        choices=Profile.PENDIDIKAN,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    pekerjaan = forms.ModelChoiceField(
        required=False,
        queryset=Pekerjaan.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:pekerjaan_autocomplete')
    )
    telepon = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'telpon',
                'placeholder': 'Telpon'
            }
        )
    )
    mobile = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'mobile',
                'placeholder': 'Mobile'
            }
        )
    )
    keluarga = forms.ModelChoiceField(
        required=False,
        queryset=Keluarga.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:keluarga_autocomplete')
    )
    ayah = forms.ModelChoiceField(
        required=False,
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:user_autocomplete')
    )
    ibu = forms.ModelChoiceField(
        required=False,
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:user_autocomplete')
    )
    email = forms.CharField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'placeholder': 'Email'
            }
        )
    )
    photo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'btn btn-default image-preview-clear'
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'name')

    def clean(self):
        data = super(BaseUserForm, self).clean()

        if self.errors:
            return data

        message = 'Mohon isi Field ini'
        kewarganegaraan = data['kewarganegaraan']
        wna = data['wna']
        paspor = data['paspor']
        paspor_kadaluarsa = data['paspor_kadaluarsa']

        if kewarganegaraan == '2' and wna == '':
            self.add_error('wna', message)

        if kewarganegaraan == '2' and paspor == '':
            self.add_error('paspor', message)

        if paspor and paspor_kadaluarsa == '':
            self.add_error('paspor_kadaluarsa', message)

        return data

    def clean_email(self):
        data = super(BaseUserForm, self).clean()

        if self.errors:
            return data

        if data['email'] == '':
            data['email'] = None


class WargaCreationForm(BaseUserForm):

    def clean(self):
        data = super(WargaCreationForm, self).clean()
        if self.errors:
            return data

        return data

    def save(self, employee, *args, **kwargs):
        kwargs['commit'] = False
        data = self.cleaned_data
        user = super(WargaCreationForm, self).save(*args, **kwargs)

        try:
            username = generate_username(name=data['name'],
                                         tanggal_lahir=data['tanggal_lahir'])
        except IndexError:
            username = generate_random_string(8)

        user.username = username
        user.set_password(generate_random_string())
        user.name = data['name']
        user.email = data['email']
        user.save()

        Profile.objects.create(
            user=user, nik=data['nik'], alamat=data['alamat'], rt=data['rt'],
            rw=data['rw'], province=data['province'], regency=data['regency'],
            district=data['district'], village=data['village'],
            kode_pos=data['kode_pos'], kewarganegaraan=data['kewarganegaraan'],
            wna=data['wna'], paspor=data['paspor'],
            paspor_kadaluarsa=data['paspor_kadaluarsa'],
            kelamin=data['kelamin'], tempat_lahir=data['tempat_lahir'],
            tanggal_lahir=data['tanggal_lahir'],
            nomor_akta_lahir=data['nomor_akta_lahir'],
            golongan_darah=data['golongan_darah'], agama=data['agama'],
            status_pernikahan=data['status_pernikahan'],
            nomor_akta_nikah=data['nomor_akta_nikah'],
            tanggal_pernikahan=data['tanggal_pernikahan'],
            nomor_akta_cerai=data['nomor_akta_cerai'],
            tanggal_perceraian=data['tanggal_perceraian'],
            hubungan_keluarga=data['hubungan_keluarga'],
            penyandang_cacat=data['penyandang_cacat'], ibu=data['ibu'],
            ayah=data['ayah'], pendidikan=data['pendidikan'],
            pekerjaan=data['pekerjaan'], telepon=data['telepon'],
            mobile=data['mobile'], keluarga=data['keluarga'],
            status_penduduk=data['status_penduduk'],
            status_tempat_tinggal=data['status_tempat_tinggal'],
            photo=data['photo']
        )
        UserLogs.objects.create(
            user=employee,
            user_edited=user,
            action=UserLogs.ACTION.created
        )
        return user


class WargaEditForm(BaseUserForm):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
                'placeholder': 'Username'
            }
        )
    )

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        data = self.cleaned_data
        user = super(WargaEditForm, self).save(*args, **kwargs)
        user.username = data['username']
        user.name = data['name']
        user.email = data['email']
        user.save()
        user.profile.nik = data['nik']
        user.profile.alamat = data['alamat']
        user.profile.rt = data['rt']
        user.profile.rw = data['rw']
        user.profile.province = data['province']
        user.profile.district = data['district']
        user.profile.regency = data['regency']
        user.profile.village = data['village']
        user.profile.kode_pos = data['kode_pos']
        user.profile.kewarganegaraan = data['kewarganegaraan']
        user.profile.wna = data['wna']
        user.profile.paspor = data['paspor']
        user.profile.paspor_kadaluarsa = data['paspor_kadaluarsa']
        user.profile.kelamin = data['kelamin']
        user.profile.tempat_lahir = data['tempat_lahir']
        user.profile.tanggal_lahir = data['tanggal_lahir']
        user.profile.nomor_akta_lahir = data['nomor_akta_lahir']
        user.profile.golongan_darah = data['golongan_darah']
        user.profile.agama = data['agama']
        user.profile.status_pernikahan = data['status_pernikahan']
        user.profile.nomor_akta_nikah = data['nomor_akta_nikah']
        user.profile.tanggal_pernikahan = data['tanggal_pernikahan']
        user.profile.nomor_akta_cerai = data['nomor_akta_cerai']
        user.profile.tanggal_perceraian = data['tanggal_perceraian']
        user.profile.hubungan_keluarga = data['hubungan_keluarga']
        user.profile.penyandang_cacat = data['penyandang_cacat']
        user.profile.ibu = data['ibu']
        user.profile.ayah = data['ayah']
        user.profile.pendidikan = data['pendidikan']
        user.profile.pekerjaan = data['pekerjaan']
        user.profile.telepon = data['telepon']
        user.profile.mobile = data['mobile']
        user.profile.keluarga = data['keluarga']
        user.profile.status_penduduk = data['status_penduduk']
        user.profile.status_tempat_tinggal = data['status_tempat_tinggal']
        user.profile.photo = data['photo']
        user.profile.save()
        print 'PASSS'
        return user


class WargaFilterForm(forms.Form):
    start = forms.DateField(input_formats=["%Y/%m/%d"], label="Start Date")
    end = forms.DateField(input_formats=["%Y/%m/%d"], label="End Date")

    def clean(self):
        cleaned_data = super(WargaFilterForm, self).clean()

        if self.errors:
            return cleaned_data

        if cleaned_data['start'] > cleaned_data['end']:
            self.add_error('start', "Start time can't be greater than end time")

    pekerjaan = forms.ModelChoiceField(
        required=False,
        queryset=Pekerjaan.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:users:pekerjaan_autocomplete')
    )

