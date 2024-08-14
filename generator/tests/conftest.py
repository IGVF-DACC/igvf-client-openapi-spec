import pytest

import json


@pytest.fixture
def raw_schemas():
    with open('./generator/tests/schemas.json') as f:
        schemas = json.load(f)
    return schemas


@pytest.fixture
def raw_embedded_fields():
    with open('./generator/tests/rawembedded.json') as f:
        raw_embedded_fields = json.load(f)
    return raw_embedded_fields    