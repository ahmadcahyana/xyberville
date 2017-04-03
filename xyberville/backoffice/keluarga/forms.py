from django import forms
from xyberville.apps.users.models import User
from xyberville.apps.keluarga.models import Keluarga
from xyberville.apps.logs.models import KeluargaLogs
from xyberville.apps.regions.models import Province, Regency, District, Village
from dal import autocomplete, forward


class BaseKeluargaForm(forms.ModelForm):
    nomor_kk = forms.CharField(
        label='Nomor KK',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nomor KK'
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
        label='RT',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'RT'
            }
        )
    )
    rw = forms.CharField(
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
    telepon = forms.CharField(
        label='Telepon',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telepon'
            }
        )
    )
    mobile = forms.CharField(
        label='Mobile Phone',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Phone'
            }
        )
    )
    kepala_keluarga = forms.ModelChoiceField(
        required=False,
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:user_autocomplete')
    )

    class Meta:
        model = Keluarga
        fields = ('nomor_kk', 'kepala_keluarga', 'alamat', 'rt', 'rw',
                  'province', 'regency', 'district', 'village', 'telepon',
                  'mobile')


class KeluargaCreationForm(BaseKeluargaForm):

    def save(self, employee, *args, **kwargs):
        kwargs['commit'] = False
        data = self.cleaned_data
        keluarga = super(KeluargaCreationForm, self).save(*args, **kwargs)
        keluarga.nomor_kk = data['nomor_kk']
        keluarga.kepala_keluarga = data['kepala_keluarga']
        keluarga.alamat = data['alamat']
        keluarga.rt = data['struktur_organisasi']
        keluarga.rw = data['rw']
        keluarga.province = data['province']
        keluarga.regency = data['regency']
        keluarga.district = data['district']
        keluarga.village = data['village']
        keluarga.telepon = data['telepon']
        keluarga.mobile = data['mobile']
        keluarga.save()

        KeluargaLogs.objects.create(
            user=employee,
            keluarga=keluarga,
            action=KeluargaLogs.ACTION.created
        )

        return keluarga


class KeluargaEditForm(BaseKeluargaForm):
    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        data = self.cleaned_data
        keluarga = super(KeluargaEditForm, self).save(*args, **kwargs)
        keluarga.nomor_kk = data['nomor_kk']
        keluarga.kepala_keluarga = data['kepala_keluarga']
        keluarga.alamat = data['alamat']
        keluarga.rt = data['struktur_organisasi']
        keluarga.rw = data['rw']
        keluarga.telepon = data['telepon']
        keluarga.mobile = data['mobile']
        keluarga.province = data['province']
        keluarga.regency = data['regency']
        keluarga.district = data['district']
        keluarga.village = data['village']
        keluarga.save()

        return keluarga
