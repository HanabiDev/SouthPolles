#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^registro/$', 'frontend.views.register_person', name='registry'),
    url(r'^elegir-prueba/$', 'frontend.views.list_polls', name='list_polls'),
    url(r'^iniciar-prueba/$', 'frontend.views.load_poll', name='load_poll'),
    url(r'^diligenciamiento/(?P<section_id>\d+)/$', 'frontend.views.serve_section', name='serve_section'),
    url(r'^guardar/(?P<section_id>\d+)/$', 'frontend.views.save_section', name='save_section' ),
    url(r'^diligenciamiento/final/$', 'frontend.views.thanks', name='thanks'),
    url(r'^dispose-info/$', 'frontend.views.dispose_info', name='dispose_info'),
)