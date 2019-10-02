import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_memcached_config(host):
    f = host.file('/etc/memcached.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('-l 127.0.0.1')
    assert f.contains('-c 1024')
    assert f.contains('-p 11211')
    assert f.contains('-m 64')


def test_memcached_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('memcached').is_enabled
    assert host.service('memcached').is_running
