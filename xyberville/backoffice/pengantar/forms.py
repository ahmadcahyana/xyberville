from django import forms
from xyberville.apps.users.models import User
from xyberville.apps.arsip.models import Pengantar, Klasifikasi
from dal import autocomplete, forward


class PengantarForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        required=False,
        queryset=User.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='backoffice:user_autocomplete')
    )
    keperluan = forms.ChoiceField(Pengantar.KEPERLUAN)
    lainnya = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Keperluan'
            }
        )
    )

    class Meta:
        model = Pengantar
        fields = ('jenis', 'nomor_surat', 'user', 'keperluan', 'lainnya')


class PengantarCreationForm(PengantarForm):

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        data = self.cleaned_data
        pengantar = super(PengantarCreationForm, self).save(*args, **kwargs)
        pengantar.jenis = Klasifikasi.objects.first()
        pengantar.nomor_surat = 'XYZ2434'
        pengantar.user = data['user']
        pengantar.keperluan = data['keperluan']
        pengantar.lainnya = data['lainnya']
        pengantar.save()

        return pengantar
