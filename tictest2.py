import pytest
@pytest.fixture
def tester():
    name = "suvanjan"
    contact = 9825676700
    return [name, contact]

def testing_1(tester):
    first_name = "suvanjan"
    assert tester[0] == first_name

def testing_2(tester):

    contact_num = 9825676700
    assert tester[1] == contact_num