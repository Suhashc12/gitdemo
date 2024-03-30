import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing 1st")
    yield
    print("I will be last")

