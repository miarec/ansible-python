# ansible-python
![CI](https://github.com/miarec/ansible-python/actions/workflows/ci.yml/badge.svg?event=push)

Ansible role for installing a particular version of Python from source.


Role Variables
--------------

- `python_version`: The version of python to install
- `python_verify_gpg_signature`: If enabled, then GPG signature is verified for the downloaded tarball.
- `python_gpg_key_id`: GPG key id used to sign python tarball, optional. The known keys are stored in vars/main.yml. You need to set this option only if the requested python version is not known yet.
- `python_force_install`: Install again even if the specified version is already found


Example Playbook
----------------

eg:

``` yaml
    - name: Install python
      hosts: localhost
      become: true
      roles:
        - role: ansible-python
          python_version: 3.5.3
          python_verify_gpg_signature: true
```

The above playbook will install python version 3.5.3.

The role can be used multiple times with different value of
`python_version` to install different versions. This can be useful for
setting up an environment for testing a python lib against multiple
versions by using tox for eg.


## Testing

This role uses [Molecule](https://molecule.readthedocs.io/) with Docker for testing.
[uv](https://docs.astral.sh/uv/) is used for dependency management.

### Prerequisites

- Docker
- uv (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Running Tests

```bash
# Run full test suite (install from source)
uv run molecule test

# Run install from package scenario
uv run molecule test -s install-from-repo

# Test against specific distro
MOLECULE_DISTRO=ubuntu2404 uv run molecule test
MOLECULE_DISTRO=rockylinux9 uv run molecule test

# Test specific Python version (source scenario only)
MOLECULE_PYTHON_VERSION=3.11.7 uv run molecule test
```

### Available Distros

| Distribution   | Variable Value  |
|----------------|-----------------|
| Ubuntu 22.04   | `ubuntu2204`    |
| Ubuntu 24.04   | `ubuntu2404`    |
| Rocky Linux 9  | `rockylinux9`   |
| RHEL 9         | `rhel9`         |

### Linting

```bash
uv run ansible-lint
```
