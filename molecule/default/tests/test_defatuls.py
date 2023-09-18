import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

python_version = os.environ.get('MOLECULE_PYTHON_VERSION', '3.8.16')



def test_files(host):
    files = [
        "/usr/local/bin/python{}".format(".".join(python_version.split('.')[:2]))
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file
