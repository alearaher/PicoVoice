from collections.abc import Sequence
from math import factorial
from math import pow, sqrt, erf
from math import pi as Pi


def prob_rain_more_than_n_normal_aprox(p: Sequence[float], n: int)->float:
    result = 0.0
   
    #Assuming a normal distribution of the days it rains, this should still hold
    #barring the case where there are no extreme outliers or additional weights 
    #(which is not the case in rainy days in vancouver, it rains a lot anyways)

    u = sum(p)
    variance = sum(Pi * (1 - Pi) for Pi in p)
    sigma = sqrt(variance)
    z = (n + 0.5 - u)/ sigma
    result = 1- (0.5*erf(z/sqrt(2)))

    return result

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
