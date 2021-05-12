import pytest
import requests
import os
import json

import requests.exceptions as ex
from questlog.generated.models.adventure import Adventure
from questlog.encoder import JSONEncoder


def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True
    except ex.ConnectionError:
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
    response = requests.get(f"{http_service}/adventure")

    assert response.status_code == 200


@pytest.mark.integration
def test_get_adventure_guid(http_service):
    response = requests.get(f"{http_service}/adventure/some_id")

    assert response.status_code == 200


def test_post_adventure(http_service):
    body = Adventure()
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = requests.post(
        f"{http_service}/adventure",
        headers=headers,
        data=json.dumps(body, cls=JSONEncoder),
    )

    assert response.status_code == 200
