from django.conf.urls import patterns, include, url
from django.contrib import admin
from ibvalid import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ibanbic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main),
    url(r'^validate/$', views.validate)
)
