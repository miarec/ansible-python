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
      become: yes
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




