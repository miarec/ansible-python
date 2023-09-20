import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

python_version = os.environ.get('PYTHON_VERSION')

def test_files(host):
    files = [
        "/usr/local/bin/python{}".format(".".join(python_version.split('.')[:2]))
    ]

    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_packages(host):
    if host.system_info.distribution == "ubuntu":
        packages = [
            "gcc",
            "make",
            "libssl-dev",
            "libsqlite3-dev",
            "libbz2-dev",
            "libffi-dev",
            "python3-pip"
        ]

    if host.system_info.distribution == "centos":
        packages = [
            "gcc",
            "make",
            "openssl-devel",
            "sqlite-devel",
            "bzip2-devel",
            "libffi-devel"
        ]

    for package in packages :
        p = host.package(package)
        assert p.is_installed