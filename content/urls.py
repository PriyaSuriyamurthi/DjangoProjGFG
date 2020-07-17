"""
Contains all url for content app
"""

from django.conf.urls import url, include
from content import views as content_views

urlpatterns = [
    # home Page url
    url(r'^home/$', content_views.home_view),
    url(r'^base/$', content_views.base_view),
]
