
import pytest
from django_models.django_models import django_models 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = django_models()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = django_models(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

