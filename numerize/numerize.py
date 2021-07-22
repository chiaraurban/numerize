#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from decimal import Decimal

def round_num(n, decimals):
    '''
    Params:
    n - number to round
    decimals - number of decimal places to round to
    Round number to 2 decimal places
    For example:
    10.0 -> 10
    10.222 -> 10.22
    '''
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals)

def drop_zero(n):
    '''
    Drop trailing 0s
    For example:
    10.100 -> 10.1
    '''
    n = str(n)
    return n.rstrip('0').rstrip('.') if '.' in n else n

def numerize(n, decimals=2):
    '''
    Params:
    n - number to be numerized
    decimals - number of decimal places to round to
    Converts numbers like:
    1,000 -> 1K
    1,000,000 -> 1M
    1,000,000,000 -> 1B
    1,000,000,000,000 -> 1T
    '''
    list_of_letters = ['space', 'K', 'M', 'B', 'T']
    is_negative_string = ""
    if n < 0:
        is_negative_string = "-"
    n = abs(Decimal(n))
    if n < 1000:
        return is_negative_string + str(drop_zero(round_num(n, decimals)))
    elif n >= 1000 and n < 1000000000000000:
        for i in range(1, 5):
            n1 = 1000**i
            n2 = n1 * 1000
            if n >= n1 and n < n2:
                if n % n1 == 0:
                    return is_negative_string + str(int(n / n1)) + list_of_letters[i]
                else:
                    n = n / n1
                    return is_negative_string + str(drop_zero(round_num(n, decimals))) + list_of_letters[i]
    else:
        return is_negative_string + str(n)

