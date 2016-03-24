import pytest
from fixture.application import Application
from fixture.application import Application2

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture