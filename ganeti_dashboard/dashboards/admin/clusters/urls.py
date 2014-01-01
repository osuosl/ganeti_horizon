from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from ganeti_dashboard.dashboards.admin.clusters import views

CLUSTERS = r'^(?P<cluster_hostname>[^/]+)/%s$'

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(CLUSTERS % '', views.DetailView.as_view(), name='detail'),
)
