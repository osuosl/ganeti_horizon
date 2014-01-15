from django.utils.translation import ugettext_lazy as _

import horizon


class Admin(horizon.Dashboard):
    name = _("Admin")
    slug = "admin"
    panels = ("overview", "clusters", "instances")
    default_panel = "overview"


horizon.register(Admin)
