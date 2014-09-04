from functools import reduce

_meta = ((1000, 'M'),
         (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
         (90, 'XC'), (50,'L'), (40, 'XL'), (10, 'X'),
         (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))

def romanize(number):
    def next(remain, result, radix, symbol):
        while remain >= radix:
            remain, result = (remain - radix, result + symbol)
        return remain, result

    r = reduce(lambda r, m:next(*(r+m)), _meta, (number, ''))
    return r[1]
