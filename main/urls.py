from django.conf.urls import url, include
from .views import create_view_location_person, list_view_location_person, detail_view_location_person

urlpatterns = [
    url(r'^create/$', create_view_location_person, name='home_view'),
    url(r'^list/$', list_view_location_person, name='list_view'),
    url(r'^detail/(?P<id>\d+)/$', detail_view_location_person, name='detail_view'),
]