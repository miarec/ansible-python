# Molecule test this role

Run Molecule test
```
uv run molecule test -s install-from-source
```

Run test with variable example
```
MOLECULE_DISTRO=rockylinux9 MOLECULE_PYTHON_VERSION=3.11.7 uv run molecule test -s install-from-source
```

## Variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2404`
    List of tested distros
    - `ubuntu2204`
    - `ubuntu2404`
    - `rockylinux9`
    - `rhel9`
 - `MOLECULE_PYTHON_VERSION` defines variable `python_version`, default `3.11.7`
