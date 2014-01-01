from django.core.urlresolvers import reverse
from django.conf import settings

from horizon import exceptions
from horizon import tabs
from horizon import views

from ganeti_dashboard.api import ganeti
from ganeti_dashboard.dashboards.admin.clusters import tabs as cluster_tabs


class IndexView(views.APIView):
    template_name = 'admin/clusters/index.html'

    def get_data(self, request, context, *args, **kwargs):
        return {'cluster': settings.CLUSTER}

class DetailView(tabs.TabView):
    tab_group_class = cluster_tabs.ClusterDetailTabs
    template_name = 'admin/clusters/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['cluster'] = self.get_data()
        return context

    def get_data(self):
        client = ganeti.GanetiRapiClient(
            host=self.kwargs['cluster_hostname'],
            username=settings.CLUSTER.get("username"),
            password=settings.CLUSTER.get("password")
        )
        cluster_info = {}
        try:
            cluster_info = client.GetInfo()
        except Exception as e:
            redirect = reverse('horizon:admin:clusters:index')
            exceptions.handle(self.request, e, redirect=redirect)
        return cluster_info

    def get_tabs(self, request, *args, **kwargs):
        cluster = self.get_data()
        return self.tab_group_class(request, cluster=cluster, **kwargs)