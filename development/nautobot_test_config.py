"""Dedicated settings for the plugin's isolated test environment."""

from pathlib import Path
import runpy


_BASE_CONFIG = Path(__file__).with_name("nautobot_config.py")
globals().update(runpy.run_path(_BASE_CONFIG))

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "testserver"]
DATABASES["default"]["TEST"] = {"NAME": "nautobot_dns_records_test"}
