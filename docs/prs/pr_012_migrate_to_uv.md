## Summary

Migrate to uv for dependency management, change default installation from source to package, and remove support for end-of-life distributions.

---

## Purpose

- **Reproducible builds**: Replace `pip install -r test-requirements.txt` with `uv` and `pyproject.toml` for deterministic dependency resolution
- **Simplify default behavior**: Most users want to install Python from system packages, not compile from source
- **Drop EOL support**: Remove centos7, rhel7, rhel8, rockylinux8, ubuntu2004 which are no longer maintained
- **Modernize Ansible syntax**: Replace deprecated `ansible_*` variables with `ansible_facts['*']` dictionary syntax

---

## Testing

* [x] Added/updated tests
* [x] Ran `ansible-lint`
* Notes: Ansible-lint passes with 0 failures. Molecule tests updated for both scenarios.

---

## Related Issues

N/A

---

## Changes

* Add `pyproject.toml` with uv dependency management and `uv.lock` for reproducible builds
* Update GitHub Actions CI workflow to use `uv run` instead of pip
* Change `python_install_from_source` default from `true` to `false`
* Rename molecule scenarios: `default` now tests package install, `install-from-source` tests source compilation
* Replace deprecated `ansible_distribution`, `ansible_os_family` with `ansible_facts['distribution']`, `ansible_facts['os_family']`
* Update `meta/main.yml` platforms to Ubuntu 22.04/24.04 and EL 9 only
* Add `CLAUDE.md` and `AGENTS.md` for AI coding assistant guidance
* Add comprehensive testing documentation to `README.md`
* Add `ansible.cfg` with roles_path configuration

---

## Notes for Reviewers

- The `uv.lock` file is auto-generated and provides reproducible dependency resolution
- Molecule scenarios renamed for clarity: default = package install (simpler case), install-from-source = compile from source
- Old distros removed from both CI matrix and molecule configs

---

## Docs

* [x] Updated relevant documentation (README.md, molecule/README.md, CLAUDE.md)
