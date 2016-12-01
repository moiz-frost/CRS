from django.conf.urls import url, include
from .views import create_view_location_person, list_view_location_person, detail_view_location_person, create_view_crime

urlpatterns = [
    url(r'^create-crime/$', create_view_crime, name='create-view-crime.html'),
    url(r'^create/$', create_view_location_person, name='create-view-location-person.html'),
    url(r'^list/$', list_view_location_person, name='list-view-location-person.html'),
    url(r'^detail/(?P<id>\d+)/$', detail_view_location_person, name='detail-view-location-person.html'),
]