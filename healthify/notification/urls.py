__author__ = 'dinesh'

from django.conf.urls import patterns, url
from notification.views import Notifications, ApiNotifications

urlpatterns = patterns('',
    url(r'^$', Notifications.as_view(), name='Notifications'),
    url(r'^notification', ApiNotifications.as_view(), name='NotificationsApi'),
)