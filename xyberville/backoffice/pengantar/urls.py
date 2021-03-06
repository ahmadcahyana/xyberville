from django.conf.urls import patterns, url

urlpatterns = patterns(
    'xyberville.backoffice.pengantar.views',
    url(
        r'^index/$',
        'index',
        name='index'
    ),
    url(
        r'^add/$',
        'add',
        name='add'
    ),
    url(
        r'^(?P<id>\d+)/pengantar/$',
        'print_surat_pengantar',
        name='print_surat_pengantar'
    ),
)
