import imp
import find_strings
import pytest

def test_ispresent():
    assert find_strings.ispresent("Al")

def test_nodigit():
    assert find_strings.nodigit("N7")