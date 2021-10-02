import json
from pprint import pprint
import math
from functools import cache


@cache
def factorial(num):
    return math.factorial(num)


@cache
def reverse_factorial(num):
    i = 1
    while num >= 1:
        i += 1
        num /= i
    return i - 1


def num_to_factorial_base(num):
    rep = []
    index = reverse_factorial(num)
    while index > 0:
        i_factorial = factorial(index)
        rep.append(int(num / i_factorial))
        num = int(num % i_factorial)
        index -= 1
    rep.append(0)
    return rep


def factorial_base_to_num(factorial_base):
    num = 0
    for i, digit in enumerate(reversed(factorial_base)):
        num += digit * factorial(i)
    return num


def permute(list, permutation_index):
    list_copy = list[::]
    perm_fact_base = num_to_factorial_base(permutation_index)
    assert len(perm_fact_base) <= len(list), 'Cannot permute more elements than those that exist'
    perm_fact_base = ([0] * (len(list) - len(perm_fact_base))) + perm_fact_base
    permuted_list = []
    for i in perm_fact_base:
        permuted_list.append(list_copy.pop(i))
    return permuted_list


def depermute(list):
    sorted_list = sorted(list)
    perm_fact_base = []
    for elem in list:
        perm_fact_base.append(sorted_list.index(elem))
        sorted_list.remove(elem)
    return factorial_base_to_num(perm_fact_base)


def main():
    # with open('./sample.json', 'r') as f:
    #     j = json.load(f)
    # for i in range(factorial(4)):
    #     print(i, end=', ')
    #     pprint(permute(list(range(4)), i))

    pprint(depermute(permute(list(range(1000)), 3824769307623709239883)))

if __name__ == '__main__':
    main()
