"""Custom validators for nautobot_dns_records."""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_dns_name(value):
    """Validate a DNS name."""
    for label in value.split("."):
        if label == "":
            raise ValidationError(_("DNS names may not contain empty labels."))
        if len(label) > 63:
            raise ValidationError(_("The label %(value)s is longer than allowed (> 63)"), params={"value": label})
