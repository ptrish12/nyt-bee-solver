import pytest
from solver import *


def test_unique_perms():
    assert len(get_perms_from_letters('aer')) == len(set(get_perms_from_letters('aer')))


def test_handles_double_letters():
    assert len(get_perms_from_letters('aar')) < len(get_perms_from_letters('aer'))


def test_word_length_respected():
    for i in get_perms_from_letters('aer'):
        assert len(i) >= 4 and len(i) <= 10

test_unique_perms()
test_word_length_respected()
test_handles_double_letters()
