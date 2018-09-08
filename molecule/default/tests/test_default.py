import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_git_is_installed(host):
    git = host.package("git")
    assert git.is_installed


def test_gitea_running_and_enabled(host):
    gitea = host.service("gitea")
    assert gitea.is_running
    assert gitea.is_enabled
