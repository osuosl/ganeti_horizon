from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from ganeti_dashboard import api
from ganeti_dashboard.dashboards.admin.instances import tables


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = "admin/clusters/_detail_overview.html"

    def get_context_data(self, request):
        cluster = self.tab_group.kwargs['cluster']
        return {"cluster": cluster}


class InstancesTab(tabs.TableTab):
    name = _("Instances")
    slug = "instances"
    table_classes = (tables.AdminInstancesTable,)
    template_name = "horizon/common/_detail_table.html"
    preload = False

    def get_instances_data(self):
        cluster = self.tab_group.kwargs['cluster_hostname']
        instances = []
        try:
            instances = api.ganeti.instance_list(cluster)
        except Exception as e:
            redirect = reverse('horizon:admin:instances:index')
            exceptions.handle(self.tab_group.request, e, redirect=redirect)
        return instances

class ClusterDetailTabs(tabs.TabGroup):
    slug = "cluster_details"
    tabs = (OverviewTab, InstancesTab)

