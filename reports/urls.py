#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^$', 'reports.views.home', name='report_home'),
    url(r'^login/$', 'reports.views.admin_login', name='login'),
    url(r'^logout/$', 'reports.views.admin_logout', name='logout'),
    url(r'^crear-reporte/$', 'reports.views.create_report', name='create_report'),
    url(r'^editar-reporte/(?P<report_id>\d+)/$', 'reports.views.edit_report', name='edit_report'),
    url(r'^editar-reporte/(?P<report_id>\d+)/agregar-seccion/$', 'reports.views.add_section', name='add_section'),
    url(r'^editar-reporte/(?P<report_id>\d+)/editar-seccion/(?P<section_id>\d+)/$', 'reports.views.edit_section', name='edit_section'),
    url(r'^editar-reporte/(?P<report_id>\d+)/eliminar-seccion/(?P<section_id>\d+)/$', 'reports.views.delete_section', name='delete_section'),
    url(r'^eliminar-reporte/(?P<report_id>\d+)/$', 'reports.views.delete_report', name='delete_report'),
    url(r'^agregar-observaciones/(?P<report_id>\d+)/$', 'reports.views.report_observ', name='report_observ'),
)