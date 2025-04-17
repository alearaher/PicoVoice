from collections.abc import Sequence
from math import factorial
from math import pow, sqrt, erf
from math import pi as Pi
import random


def prob_rain_more_than_n_normal_aprox(p: Sequence[float], n: int)->float:
    result = 0.0
   
    #Assuming a normal distribution of the days it rains, this should still hold
    #barring the case where there are no extreme outliers or additional weights 
    #(which is not the case in rainy days in vancouver, it rains a lot anyways)

    u = sum(p)
    variance = sum(Pi * (1 - Pi) for Pi in p)
    sigma = sqrt(variance)
    z = (n + 0.5 - u)/sigma
    result = 1.0 - (0.5*erf(z/sqrt(2)))

    return result

def prob_rain_more_than_n(p: Sequence[float], n: int)->float:
 

    result = 1.0 
    p_sorted = sorted(p, reverse=True) #to get the maximum probabilities first, since we are not interested in the time period for this
    
    for p in p_sorted[0:n]:
        result *= p


    return result

 

#Creating a 365 array of probabilities of rain for Vancouver
p = [random.uniform(0.1, 0.9) for _ in range(365)]
#print (p)
chance_normal = prob_rain_more_than_n_normal_aprox(p, 100)
chance = prob_rain_more_than_n_normal_aprox(p, 100)
print(chance)
print(chance_normal)

