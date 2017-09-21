
import pytest
from fixture.application_contact import Application
from fixture.application import Application

@pytest.fixture (scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

