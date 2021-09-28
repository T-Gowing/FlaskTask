import pytest
import app
from controllers import fruits

@pytest.fixture
def api(monkeypatch):
    test_fruits = [
        {'id': 1, 'fruit': 'Test Fruit 1', 'taste': 'Test Taste 1', 'colour': 'Test Colour 1'},
        {'id': 2, 'fruit': 'Test Fruit 2', 'taste': 'Test Taste 2', 'colour': 'Test Colour 2'}
    ]
    monkeypatch.setattr(fruits, "fruits", test_fruits)
    api = app.app.test_client()
    return api