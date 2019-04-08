import argparse
from typing import List


def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes() -> List[int]:
    primes = []
    n = 101
    while len(primes) < 26:
        if is_prime(n):
            primes.append(n)
            print('found {} primes'.format(len(primes)))
        n += 1
    return primes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('message')
    args = parser.parse_args()

    primes_list = get_primes()
    primes = [primes_list[ord(s) - ord('A')] for s in args.message]
    prime_products = []

    for i in range(len(primes) - 1):
        prime_products.append(primes[i] * primes[i + 1])

    print(' '.join([str(x) for x in prime_products]))


if __name__ == '__main__':
    main()