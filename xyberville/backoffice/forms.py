from dal import autocomplete
from django.core.exceptions import ObjectDoesNotExist

from xyberville.apps.users.models import User
from xyberville.apps.keluarga.models import Keluarga
from xyberville.apps.pekerjaan.models import Pekerjaan
from xyberville.apps.regions.models import Province, District, Regency, Village


class UserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return User.objects.none()

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

    def get_result_label(self, item):
        nik = item.profile.nik
        if not nik:
            nik = '-----'
        return '%s ( %s )' % (item.name, nik)


class KeluargaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Keluarga.objects.none()

        qs = Keluarga.objects.all()

        if self.q:
            qs = qs.filter(nomor_kk__icontains=self.q)

        return qs

    def get_result_label(self, item):
        return item.nomor_kk


class PekerjaanAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Pekerjaan.objects.none()

        qs = Pekerjaan.objects.all()

        if self.q:
            qs = qs.filter(nama__icontains=self.q)

        return qs


class ProvinceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Province.objects.none()

        qs = Province.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    def get_result_label(self, item):
        return '%s [%s]' % (item.name, item.code)


class RegencyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Regency.objects.none()

        qs = Regency.objects.all()
        try:
            province = self.forwarded.get('province', None)
            province_code = Province.objects.get(id=province)
        except ObjectDoesNotExist:
            province = None
            province_code = None

        if province:
            qs = qs.filter(province=province_code)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    def get_result_label(self, item):
        return '%s [%s]' % (item.name, item.code)


class DistrictAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return District.objects.none()

        qs = District.objects.all()

        regency = self.forwarded.get('regency', None)
        regency_code = Regency.objects.get(id=regency)

        if regency:
            qs = qs.filter(regency=regency_code)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    def get_result_label(self, item):
        return '%s [%s]' % (item.name, item.code)


class VillageAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Village.objects.none()

        qs = Village.objects.all()

        district = self.forwarded.get('district', None)
        district_code = District.objects.get(id=district)

        if district:
            qs = qs.filter(district=district_code)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    def get_result_label(self, item):
        return '%s [%s]' % (item.name, item.code)
