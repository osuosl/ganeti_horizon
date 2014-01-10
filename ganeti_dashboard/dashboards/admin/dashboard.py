from django.utils.translation import ugettext_lazy as _

import horizon


class Admin(horizon.Dashboard):
    name = _("Admin")
    slug = "admin"
    panels = ("clusters", "instances")
    default_panel = "clusters"


horizon.register(Admin)
