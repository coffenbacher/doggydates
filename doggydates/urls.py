from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'doggydates.views.customers', name='customers'),
    url(r'^changes$', 'doggydates.views.changes', name='changes'),
    url(r'^schedule$', 'doggydates.views.schedule', name='schedule'),
    url(r'^billing$', 'doggydates.views.billing', name='billing'),
    # url(r'^doggydates/', include('doggydates.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
