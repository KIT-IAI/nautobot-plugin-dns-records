# Nautobot DNS Records

## Overview
This plugin allows managing DNS record in Nautobot.
The following record types are actually supported:
* A / AAAA Records
* CNAME Records
* PTR Records
* LOC Records
* SSHFP Records
* SRV Records

## Development

The development environment uses Docker for the auxiliary containers and Poetry for Python dependencies.

The following requirements are needed for a setup:
* docker
* Docker Compose
* poetry
* Python 3.11

* Setup steps:
1. `poetry env use python3.11`
2. `poetry install`
3. `docker compose -f development/docker-compose.yml up -d`
4. `poetry run python development/manage.py -c development/nautobot_config.py migrate`
5. `poetry run python development/manage.py -c development/nautobot_config.py runserver`

## Setup

1. Install the `nautobot-dns-records` package to your nautobot virtual environment
2. Run `nautobot-server migrate`

## License

This code is licensed under the [Apache License 2.0](LICENSE)

Copyright 2022, Copyright Owner: Karlsruhe Institute of Technology (KIT)

Author: Daniel Bacher

Contact: daniel.bacher@kit.edu, Institute of Software Development
