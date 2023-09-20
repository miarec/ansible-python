import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_files(host):
    files = [
        "/usr/bin/python3"
    ]

    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file

def test_packages(host):
    if host.system_info.distribution == "ubuntu":
        packages = [
            "python3",
            "python3-dev",
            "python3-venv"
        ]

    if host.system_info.distribution == "centos":
        packages = [
            "epel-release",
            "python3",
            "python3-devel",
            "python36-virtualenv"
        ]

    for package in packages :
        p = host.package(package)
        assert p.is_installed
