import sys
from hypothesis import given, assume
from hypothesis.strategies import integers, lists, functions

sys.path.append(r'C:\Users\ophir\PycharmProjects\json_compressor')
from base.mixed_base import MixedBase


@given(integers(min_value=0), functions(like=lambda x: (x+1), returns=integers(min_value=1), pure=True))
def test_base_deconversion_inverts_conversion_all_funcs(num, base_func):
    base = MixedBase(base_func)
    assert base.to_int(base.from_int(num)) == num
