from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from ganeti_dashboard.dashboards.project.instances import views


urlpatterns = patterns(
    'ganeti_dashboard.dashboards.project.instances.views',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
