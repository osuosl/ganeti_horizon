from django.core.urlresolvers import reverse

from horizon import exceptions
from horizon import tabs
from horizon import tables

from ganeti_dashboard import api
from ganeti_dashboard.dashboards.admin.clusters import tables as cluster_tables
from ganeti_dashboard.dashboards.admin.clusters import tabs as cluster_tabs


class IndexView(tables.DataTableView):
    table_class = cluster_tables.AdminClustersTable
    template_name = 'admin/clusters/index.html'

    def get_data(self, *args, **kwargs):
        return api.ganeti.cluster_list()


class DetailView(tabs.TabbedTableView):
    tab_group_class = cluster_tabs.ClusterDetailTabs
    template_name = 'admin/clusters/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['cluster'] = self.get_data()
        return context

    def get_data(self):
        cluster_info = {}
        try:
            hostname = self.kwargs.get('cluster_hostname')
            cluster_info = api.ganeti.cluster_info(hostname)
        except Exception as e:
            redirect = reverse('horizon:admin:clusters:index')
            exceptions.handle(self.request, e, redirect=redirect)
        return cluster_info

    def get_tabs(self, request, *args, **kwargs):
        cluster = self.get_data()
        return self.tab_group_class(request, cluster=cluster, **kwargs)