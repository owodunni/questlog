import pytest
import pprint
import json
from questlog.generated.models import Adventure
from questlog.encoder import JSONEncoder

serialized_adventure = '{"name": "Oland"}'
adventure_name = "Oland"


@pytest.fixture
def some_adventure() -> Adventure:
    return Adventure(name=adventure_name)


def test_serialize_adventure(some_adventure):
    assert serialized_adventure == json.dumps(some_adventure, cls=JSONEncoder)


def test_deserialize_adventure(some_adventure):
    adventure_dict = json.loads(serialized_adventure)
    assert some_adventure == Adventure.from_dict(adventure_dict)
