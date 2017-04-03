from django.conf.urls import patterns, url, include
from xyberville.backoffice.forms import (
    UserAutocomplete,
    KeluargaAutocomplete,
    PekerjaanAutocomplete,
    ProvinceAutocomplete,
    RegencyAutocomplete,
    DistrictAutocomplete,
    VillageAutocomplete
)


urlpatterns = patterns(
    'xyberville.backoffice.views',
    url(r'^login$', 'login_view', name='login_view'),
    url(r'^logout$', 'logout_view', name='logout_view'),
    url(r'^$', 'index', name='index'),
    url(
        r'^user-autocomplete/$',
        UserAutocomplete.as_view(),
        name='user_autocomplete',
    ),
    url(
        r'^keluarga-autocomplete/$',
        KeluargaAutocomplete.as_view(),
        name='keluarga_autocomplete',
    ),
    url(
        r'^pekerjaan-autocomplete/$',
        PekerjaanAutocomplete.as_view(),
        name='pekerjaan_autocomplete',
    ),
    url(
        r'^province-autocomplete/$',
        ProvinceAutocomplete.as_view(),
        name='province_autocomplete',
    ),
    url(
        r'^regency-autocomplete/$',
        RegencyAutocomplete.as_view(),
        name='regency_autocomplete',
    ),
    url(
        r'^district-autocomplete/$',
        DistrictAutocomplete.as_view(),
        name='district_autocomplete',
    ),
    url(
        r'^village-autocomplete/$',
        VillageAutocomplete.as_view(),
        name='village_autocomplete',
    ),

    url(
        r'users/', include(
            'xyberville.backoffice.users.urls', namespace='users'
        )
    ),
    url(
        r'keluarga/', include(
            'xyberville.backoffice.keluarga.urls', namespace='keluarga'
        )
    ),
    url(
        r'pengantar/', include(
            'xyberville.backoffice.pengantar.urls', namespace='pengantar'
        )
    ),
)
