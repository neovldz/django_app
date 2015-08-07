from django.contrib import admin
from django.conf.urls import url, include

from soccer import urls as soccer_urls
from football import urls as football_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^soccer-api/', include(soccer_urls)),
    url(r'^football-api/', include(football_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))  # noqa
]
