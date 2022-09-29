"""EX05 Testing Setup."""

__author__ = "730569341" 

from utils import only_evens
from utils import sub
from utils import concat 

def test_only_evens() -> None:
    """Test if list contains any even numbers."""
    # one edge case
    assert only_evens(a_list, 0) == None
    # two use cases
    a_list = [1, 2, 3, 4, 5, 6, 7]
    assert only_evens(a_list) == [2, 4, 6]

def test_sub() -> None:


def test_concat() -> None:
