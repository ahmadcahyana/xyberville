from django.conf.urls import patterns, url

urlpatterns = patterns(
    'xyberville.backoffice.users.views',
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
        r'^(?P<id>\d+)/$',
        'detail',
        name='detail'
    ),
    url(
        r'^(?P<id>\d+)/edit/$',
        'edit',
        name='edit'
    ),
    url(
        r'^(?P<id>\d+)/pengantar/$',
        'print_surat_pengantar',
        name='print_surat_pengantar'
    ),
)
