import pytest
import requests
import os

from requests.exceptions import ConnectionError


def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True
    except ConnectionError:
        return False


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(str(pytestconfig.rootdir), "docker-compose.yml")


@pytest.fixture(scope="session")
def http_service(docker_ip, docker_services):
    """Ensure that HTTP service is up and responsive."""

    # `port_for` takes a container port and returns the corresponding host port
    port = docker_services.port_for("questlog", 8080)
    url = f"http://{docker_ip}:{port}"
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1, check=lambda: is_responsive(url)
    )
    return url


@pytest.mark.integration
def test_get_adventure(http_service):

    headers = {
        "Accept": "application/json",
    }
    response = requests.get(f"{http_service}/adventure", headers)

    assert response.status_code == 200
