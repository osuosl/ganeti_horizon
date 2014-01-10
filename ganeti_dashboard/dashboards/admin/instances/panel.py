from django.utils.translation import ugettext_lazy as _

import horizon

from ganeti_dashboard.dashboards.admin import dashboard


class Instances(horizon.Panel):
    name = _("Instances")
    slug = "instances"


dashboard.Admin.register(Instances)
