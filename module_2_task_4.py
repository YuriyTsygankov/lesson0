numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []
not_primes = []
for i in numbers:
    number_of_divisors = 0
    for j in numbers:
        if i % j == 0:
            number_of_divisors = number_of_divisors + 1
    if number_of_divisors == 2:
        primes.append(numbers[i - 1])
    if number_of_divisors > 2:
        not_primes.append(numbers[i - 1])
print('numbers:', numbers)
print('Primes:', primes)
print('Not_primes:', not_primes)
