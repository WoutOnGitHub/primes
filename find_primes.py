from math import sqrt, floor

def is_prime(num):
    for i in range(2, floor(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

primes_count = 0
num_to_check = 1
with open("primes.txt", "w") as f:
    while primes_count < 1_000_000:
        if is_prime(num_to_check):
            f.write(f"{num_to_check}\n")
            primes_count += 1
        num_to_check += 1