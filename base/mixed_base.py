class MixedBase:
    def __init__(self, base_func):
        self._base_func = base_func

    def from_int(self, num):
        rep = []
        i = 0
        while num > 0:
            base = self._base_func(i)
            rep.append(num % base)
            num //= base
            i += 1
        return rep

    def to_int(self, dig_list):
        num_len = len(dig_list)
        dig_list = reversed(dig_list)
        result = 0
        for i, digit in enumerate(dig_list):
            if i > 0:
                result *= self._base_func(num_len - i - 1)
            result += digit
        return result