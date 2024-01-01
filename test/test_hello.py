"""This is a test of the hell() function"""

from hello import hello
from hello import return_hunter


def test_hello():
    assert hello() == 5

def test_return_hunter():
    assert return_hunter() == "Hunter"
