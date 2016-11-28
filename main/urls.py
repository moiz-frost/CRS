from django.conf.urls import url, include
from .views import home_view, list_view

urlpatterns = [
    url(r'^$', home_view, name='home_view'),
    url(r'^list/$', list_view, name='list_view'),
    #url(r'^(?P<id>\d+)/$', list_view, name='detail'),
]