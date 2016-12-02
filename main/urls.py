from django.conf.urls import url
from .views import list_view_location, detail_view_location, \
    create_view_crime_committed, list_view_crime_committed, list_view_victim, list_view_suspect, list_view_crime, \
    list_view_crime_category, detail_view_victim, detail_view_suspect, detail_view_crime, detail_view_crime_category

urlpatterns = [
    url(r'^create-crime-committed/$', create_view_crime_committed, name='create-view-crime-committed.html'),
    url(r'^list-crime-committed/$', list_view_crime_committed, name='list-view-crime-committed.html'),
    url(r'^list-crime-category/$', list_view_crime_category, name='list-view-crime-category.html'),
    url(r'^list-crime/$', list_view_crime, name='list-view-crime.html'),
    url(r'^list-victim/$', list_view_victim, name='list-view-victim.html'),
    url(r'^list-suspect/$', list_view_suspect, name='list-view-suspect.html'),
    url(r'^list-location/$', list_view_location, name='list-view-location.html'),
    url(r'^location-detail/(?P<id>\d+)/$', detail_view_location, name='detail-view-location.html'),
    url(r'^victim-detail/(?P<id>\d+)/$', detail_view_victim, name='detail-view-victim.html'),
    url(r'^suspect-detail/(?P<id>\d+)/$', detail_view_suspect, name='detail-view-suspect.html'),
    url(r'^crime-detail/(?P<id>\d+)/$', detail_view_crime, name='detail-view-crime.html'),
    url(r'^crime-category-detail/(?P<id>\d+)/$', detail_view_crime_category, name='detail-view-crime-category.html'),
]
