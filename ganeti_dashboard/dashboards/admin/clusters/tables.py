# from django.template.defaultfilters import title
from django.utils.translation import ugettext_lazy as _

from horizon import tables

class AdminClustersTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"),
        link="horizon:admin:clusters:detail")
    version = tables.Column("software_version", verbose_name=_("Version"))
    master = tables.Column("master", verbose_name=_("Master Node"))

    class Meta:
        name = "clusters"
        verbose_name = _("Clusters")

    def get_object_id(self, datum):
        return datum['name']