from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from ganeti_dashboard.dashboards.admin.clusters import views

BASE = r'^clusters/%s$'
CLUSTERS = BASE % '(?P<cluster_hostname>[^/]+)/%s'

urlpatterns = patterns('',
    url(BASE % '', views.IndexView.as_view(), name='index'),
    url(CLUSTERS % '', views.DetailView.as_view(), name='detail'),
)