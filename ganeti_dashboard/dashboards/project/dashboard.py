from django.utils.translation import ugettext_lazy as _

import horizon


class Project(horizon.Dashboard):
    name = _("Project")
    slug = "project"
    panels = ()  # Add your panels here.
    default_panel = ''  # Specify the slug of the dashboard's default panel.


horizon.register(Project)
