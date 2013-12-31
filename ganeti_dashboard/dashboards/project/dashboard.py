from django.utils.translation import ugettext_lazy as _

import horizon


class Project(horizon.Dashboard):
    name = _("Project")
    slug = "project"
    panels = ('instances',)
    default_panel = 'instances'


horizon.register(Project)
