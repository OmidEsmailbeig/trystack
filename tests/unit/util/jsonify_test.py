import json
from trystack.util import jsonify


def test_jsonify():
    result = jsonify(
        state={'data': 'test'},
        metadata={'metadata': 'test'},
        headers={'X-TryStack-Header', 'test'},
        status=200
    )
    assert type(result) is tuple
    assert result[0] == {'data': 'test', 'metadata': 'test'}
    assert result[1] == 200
    assert result[2] == {'X-TryStack-Header', 'test'}
