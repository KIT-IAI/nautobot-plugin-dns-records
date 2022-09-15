# Nautobot DNS Records

## Overview
This plugin allows to manage DNS records in Nautobot

## Development

The Development Environment is a docker based.

**Setup:**
1. ``poetry install --all-extras``
2. ``poetry shell``
3. copy [creds.example.env](development/creds.example.env) to ``development/creds.env`` and update the passwords
4. ``invoke build``
5. ``invoke start``

## License

This code is licensed under the [Apache License 2.0](LICENSE)

The following files are copyrighted by Network to Code, LLC ([Source](https://github.com/nautobot/nautobot-plugin-golden-config)):
* [development/](development)
* [tasks.py](tasks.py)
* [pyproject.toml](pyproject.toml)(Parts)
