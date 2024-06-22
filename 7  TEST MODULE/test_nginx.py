import testinfra

def test_nginx_is_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_is_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_is_listening_on_port_80(host):
    socket = host.socket("tcp://0.0.0.0:80")
    assert socket.is_listening