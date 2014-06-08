from django.conf.urls import patterns, include, url
#from apps.surveys import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#import settings

admin.autodiscover()
#media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'apps.surveys.views.Index', name='survey_index'),
	url(r'^survey/(?P<id>\d+)/$', 'apps.surveys.views.SurveyDetail', name='survey_detail'),
	url(r'^confirm/(?P<uuid>\w+)/$', 'apps.surveys.views.Confirm', name='confirmation'),


	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

# media url hackery. le sigh. 
#urlpatterns += patterns('',
#    (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
#     { 'document_root': settings.MEDIA_ROOT, 'show_indexes':True }),
#)

