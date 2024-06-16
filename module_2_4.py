numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = bool
couse = 0
for i in numbers:
    for j in range(1, i + 1):
        if i % j == 0:
            couse = couse + 1
    if couse <= 2:
        is_prime = True
        primes.append(i)
        couse = 0
    else:
        is_prime = False
        not_primes.append(i)
        couse = 0
print(primes)
print(not_primes)

