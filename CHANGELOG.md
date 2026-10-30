# Changelog

## 0.5.2 - 2026-10-30

### Changed

- Updated the locked development and test environment to Nautobot 3.2.8 and its compatible dependencies.

### Verified

- Passed all 56 Nautobot tests with 88% coverage.

## 0.5.1 - 2026-08-24

### Fixed

- Updated `python-dotenv` and `setuptools` to security-fixed versions.

## 0.5.0 - 2026-08-24

### Added

- Support and test coverage for Nautobot 3.2.3.
- Global search filters for all supported DNS record types.
- Isolated local and CI test configuration with a dedicated test database.
- API CRUD coverage using write-enabled Nautobot API tokens.
- UI access and PTR migration regression tests.

### Changed

- Updated the development stack to Python 3.10-3.14, Django 5, PostgreSQL 16, and Redis on configurable local ports.
- Updated plugin template extensions, URLs, permissions, forms, and CI for current Nautobot APIs.
- Improved DNS label validation and preservation of model `save()` arguments.

### Fixed

- Made PTR migration rollback safe by restoring and populating the legacy label column before enforcing constraints.
- Updated development dependencies, including `h11` for the security fix.
