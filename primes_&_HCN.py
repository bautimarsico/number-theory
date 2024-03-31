
class numero():
    def __init__(self,n) -> None:
        self.number = n
        
        
        divisors = 0 
        for j in range(1,n+1):
           if n%j == 0:
              divisors = divisors + 1

        self.divisors = divisors  
        
n = 100


hcn = []
primes = [2]

for j in range(n):
    for i in range(2,j):
        if j%i == 0:
            break
        if i + 1 == j:
            primes.append(j)



highest_divisors = 0
for i in range(1,n+1):
    x = numero(i)
    
    if x.divisors > highest_divisors:
            highest_divisors = x.divisors
            hcn.append(x.number)

print(primes)
print(hcn)


