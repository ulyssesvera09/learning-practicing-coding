from math import sqrt
from math import floor

def is_prime(n):
    # max value == 9999
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    square = floor(sqrt(n))
    for num in primes:
        if square < num:
            break
        if n%num == 0:
            return False
    return True

def is_circular_prime(n):
    digits = str(n)
    variants = len(digits)
    dig_str = digits*variants
    var_list = []
    for i in range(variants):
        num = dig_str[i:variants+i]
        var_list.append(int(num))
    for var in var_list:
        if is_prime(var) == False:
            return False
    return True
