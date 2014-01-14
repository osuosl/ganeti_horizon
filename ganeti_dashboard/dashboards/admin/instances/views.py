from django.core.urlresolvers import reverse
from django.conf import settings

from horizon import exceptions
from horizon import tables

from ganeti_dashboard import api
from ganeti_dashboard.dashboards.admin.instances import tables as admin_tables

class IndexView(tables.DataTableView):
    table_class = admin_tables.AdminInstancesTable
    template_name = 'admin/instances/index.html'

    def get_data(self):
        clusters = api.ganeti.cluster_list(bulk=False)
        instances = []
        try:
            for cluster in clusters:
                instances += api.ganeti.instance_list(cluster['name'])
        except Exception as e:
            redirect = reverse('horizon:admin:instances:index')
            exceptions.handle(self.request, e, redirect=redirect)
        return instances
