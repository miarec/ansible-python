import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_files(host):
    files = [
        "/usr/local/bin/python3.8"
    ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file
