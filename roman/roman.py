from functools import reduce

_Meta = ((1000, 'M'),
         (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
         (90, 'XC'), (50,'L'), (40, 'XL'), (10, 'X'),
         (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def romanize(number):
    def next(result, remain, radix, symbol):
        while remain >= radix:
            result, remain = (result + symbol, remain - radix)
        return result, remain

    r, _ = reduce(lambda r, m:next(*(r+m)), _Meta, ('', number))
    return r
