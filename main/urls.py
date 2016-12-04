from django.conf.urls import url
from .views import list_view_location, detail_view_location, \
    create_view_crime_committed, list_view_crime_committed, list_view_victim, list_view_suspect, list_view_crime, \
    list_view_crime_category, detail_view_victim, detail_view_suspect, detail_view_crime, detail_view_crime_category, \
    update_view_location, update_view_crime, update_view_crime_category, update_view_suspect, update_view_victim

urlpatterns = [

    # Create Views
    url(r'^create-crime-committed/$',
        create_view_crime_committed,
        name='create-view-crime-committed.html'),

    # List Views
    url(r'^crime-committed-list/$',
        list_view_crime_committed,
        name='list-view-crime-committed.html'),
    url(r'^crime-category-list/$',
        list_view_crime_category,
        name='list-view-crime-category.html'),
    url(r'^crime-list/$',
        list_view_crime,
        name='list-view-crime.html'),
    url(r'^victim-list/$',
        list_view_victim,
        name='list-view-victim.html'),
    url(r'^suspect-list/$',
        list_view_suspect,
        name='list-view-suspect.html'),
    url(r'^location-list/$',
        list_view_location,
        name='list-view-location.html'),

    # Detail Views
    url(r'^location-list/details/(?P<id>\d+)/$',
        detail_view_location,
        name='detail-view-location.html'),
    url(r'^victim-list/details/(?P<id>\d+)/$',
        detail_view_victim,
        name='detail-view-victim.html'),
    url(r'^suspect-list/details/(?P<id>\d+)/$',
        detail_view_suspect,
        name='detail-view-suspect.html'),
    url(r'^crime-list/details/(?P<id>\d+)/$',
        detail_view_crime,
        name='detail-view-crime.html'),
    url(r'^crime-category-list/details/(?P<id>\d+)/$',
        detail_view_crime_category,
        name='detail-view-crime-category.html'),

    # Edit Views
    url(r'^location-list/details/(?P<id>\d+)/edit/$',
        update_view_location,
        name='update-view-location'),
    url(r'^crime-list/details/(?P<id>\d+)/edit/$',
        update_view_crime,
        name='update-view-crime'),
    url(r'^crime-category-list/details/(?P<id>\d+)/edit/$',
        update_view_crime_category,
        name='update-view-crime-category'),
    url(r'^victim-list/details/(?P<id>\d+)/edit/$',
        update_view_victim,
        name='update-view-victim'),
    url(r'^suspect-list/details/(?P<id>\d+)/edit/$',
        update_view_suspect,
        name='update-view-suspect')
]
