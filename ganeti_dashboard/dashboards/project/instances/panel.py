from django.utils.translation import ugettext_lazy as _

import horizon

from project import dashboard


class Instances(horizon.Panel):
    name = _("Instances")
    slug = "instances"


dashboard.Project.register(Instances)
