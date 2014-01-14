from django.core.urlresolvers import reverse
from django.template.defaultfilters import title
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from horizon.templatetags.sizeformat import mbformat

def get_oper_state(instance):
    return str(instance['oper_state'])

def get_beparams(param):
    def get_param(instance):
        return instance['beparams'][param]
    return get_param

def get_memory(instance):
    max_mem = instance['beparams']['maxmem']
    min_mem = instance['beparams']['minmem']
    if max_mem == min_mem:
        return mbformat(max_mem)
    min_mem = mbformat(min_mem)
    max_mem = mbformat(max_mem)
    return "{min} - {max}".format(min=min_mem, max=max_mem)

def get_cluster_link(instance):
    kwargs = {'cluster_hostname': instance['cluster']}
    link = reverse("horizon:admin:clusters:detail", kwargs=kwargs)
    return link

class AdminInstancesTable(tables.DataTable):
    STATUS_CHOICES = (
        ('running', True),
        ('ADMIN_offline', True),
        ('USER_down', True),
        ('ADMIN_down', True),
        ('ERROR_up', False),
        ('ERROR_down', False),
        ('ERROR_nodedown', False),
        ('ERROR_nodeoffline', None),
        ('ERROR_wrongnode', None),
    )

    DISPLAY_CHOICES = (
        ('running', "Active"),
        ('ADMIN_offline', "Active"),
        ('USER_down', "Inactive"),
        ('ADMIN_down', "Inactive"),
        ('ERROR_up', "Active"),
        ('ERROR_down', "Inactive"),
        ('ERROR_nodedown', "Primary node down"),
        ('ERROR_nodeoffline', "Primary node offline"),
        ('ERROR_wrongnode', "On wrong node"),
    )

    STATE_DISPLAY_CHOICES = (
        ("True", "Running"),
        ("False", "Stopped"),
    )

    name = tables.Column("name", verbose_name=_("Name"))
    cluster = tables.Column("cluster", verbose_name=_("Cluster"),
        link=get_cluster_link)
    status = tables.Column("status", filters=(title,),
        verbose_name=_("Status"), status=True,
        status_choices=STATUS_CHOICES, display_choices=DISPLAY_CHOICES)
    state = tables.Column(get_oper_state, status=True,
        verbose_name=_("State"), display_choices=STATE_DISPLAY_CHOICES)
    cpus = tables.Column(get_beparams('vcpus'), verbose_name=_("CPU's"))
    memory = tables.Column(get_memory, verbose_name=_("Memory"))

    class Meta:
        name = "instances"
        verbose_name= _("Instances")

    def get_object_id(self, datum):
        return datum['name']