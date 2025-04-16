from collections.abc import Sequence
from math import factorial
from math import pow



def prob_rain_more_than_n(p: Sequence[float], n: int)->float:
    #First we need to determine all the possibilities in which n can be satisfied
    # the formula is N = days! ((n! * (days-n)!)) 
    days = 365
    N = factorial(days) / (factorial(n) * (factorial(days - n)))
     
    #now determining the probability of one or more occurances
    #if all probabilites were the same per day:
    #   (p^k)*((1-p)^(n-k))
    #p^k: sum of all succesfull probabilities
    #((1-p)^(n-k)): sum of all unsuccesfull probabilities

    sP_sum = sum(p) # succesfull probabilities
    nsP = [pow(1-x,365-n) for x in p] # not successfull probabilities
    nsP_sum = sum(nsP)

    result = sP_sum*nsP_sum


    return result


#Creating a 365 array of probabilities of rain for Vancouver
