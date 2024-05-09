# Molecule test this role


## Scenario - `default`
This will test the role installing a specific version of python3 from source

Run Molecule test
```
molecule test -s install-from-source
```

Run test with variable example
```
MOLECULE_DISTRO=centos7 molecule test
```

### Variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2204`
    List of tested distros
    - `ubuntu2204`
    - `ubuntu2004`
    - `centos7`
    - `rhel7`
    - `rhel8`
    - `rhel9`
 - `MOLECULE_PYTHON_VERSION` defines variable `python_version`, default `3.11.7`
 - `MOLECULE_ANSIBLE_VERBOSITY` 0-3 used for troubleshooting, will set verbosity of ansible output, same as `-vvv`, default `0`

## Scenario - `install-from-repo`
This will test installing python3 from package

Run Molecule test
```
molecule test
```

Run test with variable example
```
MOLECULE_DISTRO=centos7 MOLECULE_PYTHON_VERSION=3.6.10 molecule test
```

### Variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2204`
    List of tested distros
    - `ubuntu2204`
    - `ubuntu2004`
    - `centos7`
    - `rhel7`
    - `rhel8`
    - `rhel9`
 - `MOLECULE_ANSIBLE_VERBOSITY` 0-3 used for troubleshooting, will set verbosity of ansible output, same as `-vvv`, default `0`