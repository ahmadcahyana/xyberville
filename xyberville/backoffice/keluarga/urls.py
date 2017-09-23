from django.conf.urls import patterns, url


urlpatterns = patterns(
    'xyberville.backoffice.keluarga.views',
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
        'details',
        name='details'
    ),
    url(
        r'^(?P<id>\d+)/edit/$',
        'edit',
        name='edit'
    ),
)
