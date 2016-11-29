from django.conf.urls import url, include
from .views import create_view, list_view, detail_view

urlpatterns = [
    url(r'^create/$', create_view, name='home_view'),
    url(r'^list/$', list_view, name='list_view'),
    url(r'^detail/(?P<id>\d+)/$', detail_view, name='detail_view'),
]