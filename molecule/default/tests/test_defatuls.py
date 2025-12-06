import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

python_bin_path = "/usr/bin/python3"


def test_python(host):
    assert host.run(f'{python_bin_path} --version').rc == 0, "Python binary should run"

def test_python_ssl(host):
    assert host.run(f'{python_bin_path} -c "import ssl"').rc == 0, "Python must be compiled with ssl"

def test_python_sqlite3(host):
    assert host.run(f'{python_bin_path} -c "import sqlite3"').rc == 0, "Python must be compiled with sqlite3"

def test_python_bz2(host):
    assert host.run(f'{python_bin_path} -c "import bz2"').rc == 0, "Python must be compiled with bz2"
