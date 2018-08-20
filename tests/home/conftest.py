import pytest

@pytest.fixture(scope="class")
def set_up_all():
    print("Starting tests:\n")
    yield
    print("Ending tests:\n")



