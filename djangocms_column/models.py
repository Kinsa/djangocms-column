from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible

from djangocms_attributes_field.fields import AttributesField


# preserves backwards compatibility with old column values
# this is no longer editable in settings; the values are referenced in the template as well and used to set a class to match
WIDTH_CHOICES = (
    ('10%', _("10%")),
    ('25%', _("25%")),
    ('33.33%', _('33%')),
    ('50%', _("50%")),
    ('66.66%', _('66%')),
    ('75%', _("75%")),
    ('100%', _('100%')),
)

XS_WIDTH_CHOICES = (
    ('', '--'),
    ('col-xs-10pct', _("10%")),
    ('col-xs-25pct', _("25%")),
    ('col-xs-33pct', _('33%')),
    ('col-xs-50pct', _("50%")),
    ('col-xs-66pct', _('66%')),
    ('col-xs-75pct', _("75%")),
    ('col-xs-100pct', _('100%')),
)

MD_WIDTH_CHOICES = (
    ('', '--'),
    ('col-md-10pct', _("10%")),
    ('col-md-25pct', _("25%")),
    ('col-md-33pct', _('33%')),
    ('col-md-50pct', _("50%")),
    ('col-md-66pct', _('66%')),
    ('col-md-75pct', _("75%")),
    ('col-md-100pct', _('100%')),
)

LG_WIDTH_CHOICES = (
    ('', '--'),
    ('col-lg-10pct', _("10%")),
    ('col-lg-25pct', _("25%")),
    ('col-lg-33pct', _('33%')),
    ('col-lg-50pct', _("50%")),
    ('col-lg-66pct', _('66%')),
    ('col-lg-75pct', _("75%")),
    ('col-lg-100pct', _('100%')),
)


@python_2_unicode_compatible
class MultiColumns(CMSPlugin):
    """
    A plugin that has sub Column classes
    """
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )
    attributes = AttributesField()

    def __str__(self):
        plugins = self.child_plugin_instances or []
        return _(u"%s columns") % len(plugins)


@python_2_unicode_compatible
class Column(CMSPlugin):
    """
    A Column for the MultiColumns Plugin
    """
    width_xs = models.CharField(
        _("extra small width (< 768px)"),
        choices=XS_WIDTH_CHOICES,
        default=XS_WIDTH_CHOICES[0][0],
        max_length=50,
        blank=True,
    )
    width = models.CharField(
        _("small width (>= 768px if xs is set)"),
        choices=WIDTH_CHOICES,
        default=WIDTH_CHOICES[0][0],
        max_length=50
    )
    width_md = models.CharField(
        _("medium width (>= 992px)"),
        choices=MD_WIDTH_CHOICES,
        default=MD_WIDTH_CHOICES[0][0],
        max_length=50,
        blank=True,
    )
    width_lg = models.CharField(
        _("large width (>= 1200px)"),
        choices=LG_WIDTH_CHOICES,
        default=LG_WIDTH_CHOICES[0][0],
        max_length=50,
        blank=True,
    )
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )
    attributes = AttributesField()

    def __str__(self):
        return u"%s" % self.get_width_display()
