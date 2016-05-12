import math
import time

#compute primes using list difference
#from http://www.secnetix.de/olli/Python/list_comprehensions.hawk
t0 = time.clock()
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
difference = [x for x in range(2, 50) if x not in noprimes]
# print(difference)
t1 = time.clock()
print("Time for list difference:", t1 - t0)

#my own version, a little more complicated
t2 = time.clock()
# noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(1, 51) if not any([y for y in range(2, int(math.sqrt(x) + 1)) if x % y == 0])]
# print(primes)
t3 = time.clock()
print("Time for my comprehension:", t3 - t2)