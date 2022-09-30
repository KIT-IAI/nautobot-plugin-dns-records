"""Model definition for nautobot_dns_records."""

import codecs

import nautobot.ipam.models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from nautobot.core.models.generics import PrimaryModel
from nautobot.extras.utils import extras_features

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
        self.label = codecs.encode(self.label, encoding="idna").decode()
        super().save()

    def __str__(self):
        """Return the label field."""
        return self.label


@extras_features(
    "custom_fields",
    "graphql",
    "statuses",
)
class AddressRecord(PrimaryModel, Record):
    """Class that represents A and AAAA record

    Attributes:
        address (nautobot.ipam.models.IPAddress)
    """

    address = models.ForeignKey(
        nautobot.ipam.models.IPAddress,
        on_delete=models.CASCADE,
        verbose_name=_("IP Address"),
        help_text=_("Related IP Address for the record."),
    )


@extras_features(
    "custom_fields",
    "graphql",
    "statuses",
)
class CNameRecord(PrimaryModel, Record):
    """Class that represents a CNAME record

    Attributes:
        target (CharField)
    """

    target = models.CharField(
        max_length=255,
        validators=[validate_dns_name],
        verbose_name=_("DNS Alias Target"),
        help_text=_("The target of the CNAME Record"),
    )

    def save(self, *args, **kwargs):
        """Override the default django save method.

        Encodes the target field with the IDNA2003 rules
        """
        self.target = codecs.encode(self.target, encoding="idna").decode()
        super().save()


@extras_features(
    "custom_fields",
    "graphql",
    "statuses",
)
class TxtRecord(PrimaryModel, Record):
    """Class that represents a TXT record

    Attributes:
        value (CharField)
    """

    value = models.CharField(max_length=255, verbose_name=_("Value"), help_text=_("The value of the TXT Record"))
