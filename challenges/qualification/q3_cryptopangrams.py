from math import sqrt
from typing import List, Tuple


def x_find_two_products(primes_list: List[int], prime_product: int) -> Tuple[int, int]:
    for x in primes_list:
        for y in primes_list:
            if x * y == prime_product:
                return x, y
    return 0, 0


def find_two_products(prime_product: int) -> Tuple[int, int]:
    n = 2
    while True:
        if prime_product % n == 0:
            return n, prime_product // n
        n += 1


def get_decrypted_primes(all_prime_products: List[int], first_prime: int) -> List[int]:
    decrypted_primes = []
    decrypted_primes.append(first_prime)
    for prime_product in all_prime_products:
        if prime_product % decrypted_primes[-1] == 0:
            decrypted_primes.append(int(prime_product / decrypted_primes[-1]))
        else:
            raise ValueError('Not a valid starting prime')
    return decrypted_primes


def main():
    cases = int(input())
    for _case in range(cases):
        case_number = _case + 1
        max_prime, number_of_prime_products = list(map(int, input().split()))
        all_prime_products = list(map(int, input().split()))
        first_prime, second_prime = find_two_products(all_prime_products[0])
        decoded_primes = []
        if all_prime_products[1] % first_prime == 0:
            first_prime, second_prime = second_prime, first_prime
        try:
            decoded_primes = get_decrypted_primes(all_prime_products, first_prime)
        except ValueError:
            decoded_primes = get_decrypted_primes(all_prime_products, second_prime)

        sorted_primes = sorted(set(decoded_primes))
        decoded_letters = []
        for decoded_prime in decoded_primes:
            decoded_letters.append(chr(ord('A') + sorted_primes.index(decoded_prime)))
        print('Case #{}: {}'.format(case_number, ''.join(decoded_letters)))


if __name__ == '__main__':
    main()
