import math

#compute primes using set difference
#from http://www.secnetix.de/olli/Python/list_comprehensions.hawk
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
difference = [x for x in range(2, 50) if x not in noprimes]
print(difference)

#my own version, a little more complicated
primes = [x for x in range(1, 51) if not any([y for y in range(2, int(math.sqrt(x) + 1)) if x % y == 0])]
print(primes)