from django.utils.translation import ugettext_lazy as _

import horizon

from ganeti_dashboard.dashboards.project import dashboard


class Instances(horizon.Panel):
    name = _("Instances")
    slug = "instances"


dashboard.Project.register(Instances)
