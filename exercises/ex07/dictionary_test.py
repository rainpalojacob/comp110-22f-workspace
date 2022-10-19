"""Unit testing for dictionary."""

__author__ = "730569341"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count


# Testing invert function


def test_invert_dict() -> None:
    """Test if dictionary is empty."""
    a: dict[str, str]
    a: dict()
    assert invert(a) == {}



def test_invert_equals_values() -> None:
    """Test if there are equal values in dictionary."""
    with pytest.raises(KeyError):
        my_dict = {'Serena': 'Williams', 'Venus': 'Williams'}
        invert(my_dict)
    


def test_invert_key() -> None:
    """Tests if dictionary has one key."""
    a: dict[str, str]
    a = dict()
    a['Serena'] = 'Williams'
    assert invert (x) == {'Williams': 'Serena'}


# Testing favorite_color function


def test_favorite_color_dict() -> None:
    """Test if dictionary is empty."""
    a: dict[str, str]
    a: dict()
    assert favorite_color(a) == ""


def test_favorite_color_different() -> None:
    """Tests if the dictionary has different favorite colors."""
    a: dict[str, str]
    a: dict()
    a['Sky'] = 'Blue'
    a['Strawberry'] = 'Red'
    a['Road'] = 'Black'
    a['Pumpkin'] = 'Orange'
    assert favorite_color(a) == 'Red'

def test_favorite_color_tie() -> None:
    "''Test if the dictionary has a tie with favorite color."""
    a: dict[str, str]
    a: dict()
    a['Sky'] = 'Blue'
    a['Ocean'] = 'Blue'
    a['Road'] = 'Black'
    a['Screen'] = 'Black'
    assert favorite_color(a) == 'Red'


# Testing count function

def test_count_dict() -> None:
    """Test if dictionary is empty."""
    a: dict[str, str]
    a: dict()
    assert count(a) == {}


def test_count_one_value() -> None:
    """Tests for unique values."""
    a: list[str] = ['Phone', 'Book', 'Pen']
    assert count(a) == {'Great': 1, 'Good': 1, 'Wow': 1}

def test_count_multi_value() -> None:
    """Test if list contains mulitple values."""
    a: list[str] = ['Phone', 'Book','Phone', 'Book']
    assert count(x) == {'Phone': 2, 'Book': 2}