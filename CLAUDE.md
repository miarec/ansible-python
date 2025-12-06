This file provides guidance to coding agent when working with code in this repository.

## Project Overview

This is an Ansible role (`ansible-python`) for installing Python from system packages or from source. It supports multiple Linux distributions (Ubuntu, Rocky Linux, RHEL) and Python versions (3.9-3.12).

## Testing Commands

### Run Molecule Tests

Uses `uv` for dependency management. No manual dependency installation required.

**Install from package (default scenario):**
```bash
uv run molecule test
```

**Install from source:**
```bash
uv run molecule test -s install-from-source
```

**With custom distro/version:**
```bash
MOLECULE_DISTRO=rockylinux9 MOLECULE_PYTHON_VERSION=3.11.7 uv run molecule test -s install-from-source
```

### Linting

```bash
uv run ansible-lint
```

### Environment Variables for Testing

- `MOLECULE_DISTRO`: Target OS (ubuntu2204, ubuntu2404, rockylinux9, rhel9)
- `MOLECULE_PYTHON_VERSION`: Python version to install (default: 3.11.7, only for install-from-source scenario)
- `MOLECULE_ANSIBLE_VERBOSITY`: 0-3 for ansible output verbosity

## Architecture

### Two Installation Modes

1. **From Package** (`python_install_from_source: false`, default): Installs python3 packages from system repositories

2. **From Source** (`python_install_from_source: true`): Downloads Python tarball from python.org, verifies GPG signature, compiles with `--enable-optimizations --enable-shared`

### Key Files

- `tasks/main.yml`: Entry point, routes to source or package installation
- `tasks/install-source.yml`: Compiles Python from source with GPG verification
- `tasks/install-package.yml`: Installs from system packages
- `vars/main.yml`: GPG key mappings for each Python version
- `vars/RedHat.yml`, `vars/Debian.yml`: OS-specific package lists
- `files/*.key`: GPG public keys for Python release signing

### Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `python_install_from_source` | false | Compile from source vs package |
| `python_version` | 3.8.16 | Python version to install (only for source) |
| `python_verify_gpg_signature` | true | Verify downloaded tarball signature |
| `python_install_dir` | /usr/local | Installation prefix |
| `python_force_install` | false | Reinstall even if version exists |
