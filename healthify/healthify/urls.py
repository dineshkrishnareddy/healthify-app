from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^notification', include('notification.urls')),
    url(r'^api/', include('notification.urls')),
)
