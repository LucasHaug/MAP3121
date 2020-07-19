#!/usr/bin/env python3

import numpy as np
import sympy as sym
import fractions
import decimal

def mult(a, b, precision):
    result = (a * b).quantize(decimal.Decimal(10)**(-precision))

    return result

#################################################
### Main Function
#################################################


def main():
    # Parameters
    precision = 2
    context = decimal.getcontext()
    context.prec = precision

    h = fractions.Fraction(11, 35)
    k = fractions.Fraction(13, 35)
    print(f"{h} + {k} = {h + k}")

    print(decimal.getcontext())

    a = decimal.Decimal('1.25')

    d = decimal.Decimal('0.123456')

    # e = decimal.Decimal('0.45456')

    c = a * d
    # c = mult(a, d, precision)

    print(f"a + d = {c}")

    for i in range(1, 6):
        decimal.getcontext().prec = i
        print(f"{i}: {d}, {d * 1}")


#################################################
### Main Function Call
#################################################

if __name__ == "__main__":
    main()
