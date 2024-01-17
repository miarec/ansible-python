import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

python_version = os.environ.get('PYTHON_VERSION')
python_bin_path = "/usr/local/bin/python{}".format(".".join(python_version.split('.')[:2]))


def test_python(host):
    assert host.run(f'{python_bin_path} --version').rc == 0, "Python binary should run"


def test_python_ssl(host):
    assert host.run(f'{python_bin_path} -c "import ssl"').rc == 0, "Python must be compiled with ssl"

def test_python_sqlite3(host):
    assert host.run(f'{python_bin_path} -c "import sqlite3"').rc == 0, "Python must be compiled with sqlite3"

def test_python_bz2(host):
    assert host.run(f'{python_bin_path} -c "import bz2"').rc == 0, "Python must be compiled with bz2"
