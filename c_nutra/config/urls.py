from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password-reset/', include('password_reset.urls')),

    # Login / logout.
    #url(r'^register/$', 'apps.users.views.register', name='register'),
    #url('^register/', CreateView.as_view(
    #        template_name='registration/register.html',
    #       form_class=UserCreationForm,
    #        success_url='/'),
    #    name='register'),
    #(r'^login/$', 'django.contrib.auth.views.login'),
    #(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}),
    #(r'^logout/$', logout_page),

    # Accounts urls
    url(r'accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'accounts/logout/$', 'apps.users.views.user_logout', name='logout'),
    url(r'accounts/register/$', 'apps.users.views.user_register', name='register'),
    url(r'accounts/profile/$', 'apps.users.views.user_profile', name='profile'),
    url(r'encuestas/$',TemplateView.as_view(template_name='surveys/surveys.html'), name='surveys'),

    # Surveys urls
    url(r'^surveys/', include('apps.surveys.urls', namespace="surveys")),

    # Examples:
    # url(r'^$', 'c_nutra.views.home', name='home'),
    # url(r'^c_nutra/', include('c_nutra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    


)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
