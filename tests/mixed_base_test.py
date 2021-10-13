import sys
from hypothesis import given, assume
from hypothesis.strategies import integers, lists, functions
from base.mixed_base import MixedBase


@given(integers(min_value=0), functions(like=lambda x: (x+1), returns=integers(min_value=1), pure=True))
def test_base_deconversion_inverts_conversion_all_funcs(num, base_func):
    base = MixedBase(base_func)
    assert base.to_int(base.from_int(num)) == num


@given(integers(min_value=1), lists(integers(min_value=2), min_size=10))
def test_max_number(num_of_digits, base_list):
    assume(len(base_list) > num_of_digits)
    base = MixedBase.new_from_list(base_list)
    max_num = base.max_num(num_of_digits)
    assert len(base.from_int(max_num)) == num_of_digits
    assert len(base.from_int(max_num + 1)) == num_of_digits + 1
