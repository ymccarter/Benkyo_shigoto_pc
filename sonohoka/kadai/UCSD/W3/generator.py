import sys
import argparse

def is_prime(candidate):
    for n in range(2, candidate//2):
        if candidate % n == 0:
            return False
    return True

# def get_big_primes(limit):
#     n = 999999
#     count = 0
#     primes = []
#     while count < limit:
#         if is_prime(n):
#             primes.append(n)
#             count += 1
#         n += 1
#     return primes

def get_big_primes(limit):
    n = 999999
    count = 0
    while count < limit:
        if is_prime(n):
            yield n
            count += 1
        n+=1

if __name__ == "__main__":
    limit = int(sys.argv[1])
    for prime in get_big_primes(limit):
        print(prime)