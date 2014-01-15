from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from ganeti_dashboard.dashboards.admin.instances import views
from ganeti_dashboard.dashboards.admin.clusters.urls import CLUSTERS

INSTANCE = CLUSTERS % '(?P<instance>[^/]+)/%s'

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
