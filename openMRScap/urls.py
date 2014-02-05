from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
import django.views

from OMRS import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openMRScap.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$',views.index,name='index'),
    #url(r'^$',views.index,name='server'),

    #add other projects URLS
    #url(r'^OMRS/',include('OMRS.urls')),

    url(r'^$','OMRS.views.index', name='home'),

    #url(r'^server/',views.jobs.as_view(),name='server'),
    url(r'^jobs/',views.jobs.as_view(),name='jobs'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^server/$','OMRS.views.server'),
    url(r'^userprofile/$','OMRS.views.userProfile',name='userprofile'),
    url(r'^jobserversettings/$','OMRS.views.userJobSettings'), #lists just the URLS of the servers in the system
    url(r'^restricted/$', 'OMRS.views.restricted', name='restricted'), #not doing anything yet

    url(r'^setup/$', 'OMRS.views.post_server_details',name='setup'),

    #user details
    url(r'^register/$', 'OMRS.views.register', name='register'),
    url(r'^login/$', 'OMRS.views.user_login',name='login'),
    url(r'^logout/$', 'OMRS.views.user_logout', name='logout'),

    #import file
    url(r'^upload/$', 'OMRS.views.upload', name='upload'),
    )

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         django.views.static.serve,
         {'document_root': settings.MEDIA_ROOT}),
    )
