
from collections.abc import Sequence
from math import factorial

def prob_rain_more_than_n(p: Sequence[float], n: int)->float:
    #First we need to determine all the possibilities in which n can be satisfied
    # the formula is N = days! ((n! * (days-n)!)) 
    days = 365
    N = factorial(days) * (factorial(n) * (factorial(days - n)))
     


    return 0.0


print(a)