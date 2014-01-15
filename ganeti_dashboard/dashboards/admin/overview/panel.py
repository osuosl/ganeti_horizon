from django.utils.translation import ugettext_lazy as _

import horizon

from ganeti_dashboard.dashboards.admin import dashboard


class Overview(horizon.Panel):
    name = _("Overview")
    slug = "overview"


dashboard.Admin.register(Overview)
