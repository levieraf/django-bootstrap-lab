from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', 'crud.views.index'),
	url(r'^about$', 'crud.views.about'),
	url(r'^contacto/', include('contacto.urls')),
    # Examples:
    # url(r'^$', 'crud.views.home', name='home'),
    # url(r'^crud/', include('crud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
