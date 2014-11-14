#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SouthPolles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('frontend.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^builder_room/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^report', 'reports.views.create_report')

)
