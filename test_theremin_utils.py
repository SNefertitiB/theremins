# import pytest
import theremin_utils

def test_cm_to_percent_min_zero():
    target = 0.0
    minimum = theremin_utils.MIN_CM
    actual = theremin_utils.cm_to_percent(minimum)
    assert target == actual

def test_cm_to_percent_max_one():
    target = 1
    maximum = theremin_utils.MAX_CM
    actual = theremin_utils.cm_to_percent(maximum)

def test_cm_to_percent_less_than_min_zero():
    target = 0.0
    less_than_min = theremin_utils.MIN_CM - 1
    actual = theremin_utils.cm_to_percent(less_than_min)
    print(less_than_min)
    assert target == actual

def test_cm_to_percent_more_than_max_one():
    target = 1
    more_than_max = theremin_utils.MAX_CM + 1
    actual = theremin_utils.cm_to_percent(more_than_max)
    assert target == actual


test_cm_to_percent_min_zero()
test_cm_to_percent_max_one()
test_cm_to_percent_less_than_min_zero()
test_cm_to_percent_more_than_max_one()