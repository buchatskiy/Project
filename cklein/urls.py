from django.conf.urls import patterns, include, url
from django.contrib import admin
from underwear.views import main, size, buy, cart, clean, universal, del_item, contacts, thanks
from django.conf import settings
from loginsys.views import login, logout, register


urlpatterns = patterns('',
    url(r'^$', universal, {'htmlfile': 'main.html'}),
    url(r'^ALL/page/(\d+)/$', main),
    url(r'^steel/page/(\d+)/$', main, {'current_series': 'steel'}),
    url(r'^365/page/(\d+)/$', main, {'current_series': '365'}),
    url(r'^(\w{1,2})/$', size),
    url(r'^buy/$', buy),
    url(r'^pay_delivery/$', universal, {'htmlfile': 'pay_delivery.html'}),
    url(r'^cart/$', cart, {'delivery':0}),
    url(r'^cart1/$', cart, {'delivery':1}),
    url(r'^cart2/$', cart, {'delivery':2}),
    url(r'^clean/$', clean),
    url(r'^thanks/$', thanks),
    url(r'^thanks_feedback/$', universal, {'htmlfile': 'thanks_feedback.html'}),
    url(r'^contacts/$', contacts),
    url(r'^del_item/$', del_item),
    url(r'^size_table/$', universal, {'htmlfile': 'size_table.html'}),
    url(r'^promotion/$', universal, {'htmlfile': 'promotion.html'}),
    url(r'^auth/login/$', login),
    url(r'^auth/logout/$', logout),
    url(r'^auth/register/$', register),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'static/media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )