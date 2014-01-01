from django.utils.translation import ugettext_lazy as _

import horizon

from ganeti_dashboard.dashboards.admin import dashboard


class Clusters(horizon.Panel):
    name = _("Clusters")
    slug = "clusters"


dashboard.Admin.register(Clusters)
