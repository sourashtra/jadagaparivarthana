from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'matrimony.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'matrimony.views.index', name='index'),
    url(r'^save_application', 'matrimony.views.save_application', name='save_application'),
    url(r'^admin/', include(admin.site.urls)),
)
