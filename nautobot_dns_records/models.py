"""Model definition for nautobot_dns_records."""

import codecs

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from nautobot_dns_records.validators import validate_dns_name


class Record(models.Model):
    """Abstract class that represents a base dns model.

    Attributes:
        label (CharField): Name of the dns node.
        ttl (IntegerField): TTL of the dns record. The minimal value is 1 and the maximum value is 604800
    """

    label = models.CharField(
        max_length=255,
        validators=[validate_dns_name],
        verbose_name=_("DNS Label"),
        help_text=_(
            "Label for the DNS entry, maximum length for individual segments is 63 characters, total length must not exceed 255 characters."
        ),
    )
    ttl = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(604800)],
        verbose_name=_("TTL"),
        help_text=_("Time to live for the dns entry in seconds, valid values are in the range 1 - 604800."),
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """Override the default django save method.

        Encodes the label field with the IDNA2003 rules
        """
        self.label = codecs.encode(self.label, encoding="idna")
        super().save()

    def __str__(self):
        """Return the label field."""
        return self.label
