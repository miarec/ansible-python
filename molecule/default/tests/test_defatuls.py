import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

python_version = os.environ.get('PYTHON_VERSION')
python_install_from_source = os.environ.get('PYTHON_INSTALL_FROM_SOURCE')

def test_files(host):

    if python_install_from_source == 'true':
        files = [
            "/usr/local/bin/python{}".format(".".join(python_version.split('.')[:2]))
        ]
    else:
        files = [
            "/usr/bin/python3"
        ]


    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file
