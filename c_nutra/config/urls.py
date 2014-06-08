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

    # Accounts urls
    url(r'accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page':'home'}, name='logout'),
    url(r'accounts/register/$', 'apps.users.views.user_register', name='register'),
    url(r'accounts/profile/$', 'apps.users.views.user_profile', name='profile'),
    
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
