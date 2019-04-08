from math import sqrt
from typing import List, Tuple


def x_find_two_products(primes_list: List[int], prime_product: int) -> Tuple[int, int]:
    for x in primes_list:
        for y in primes_list:
            if x * y == prime_product:
                return x, y
    return 0, 0


def find_gcd(prime_product1: int, prime_product2: int) -> int:
    # Use Euclidean division
    if prime_product1 < prime_product2:
        return find_gcd(prime_product2, prime_product1)

    remainder = prime_product1 % prime_product2
    if remainder == 0:
        return prime_product2

    return find_gcd(prime_product2, remainder)


def get_decrypted_primes(all_prime_products: List[int], first_prime: int) -> List[int]:
    decrypted_primes = [first_prime]
    for prime_product in all_prime_products:
        if prime_product % decrypted_primes[-1] == 0:
            decrypted_primes.append(int(prime_product / decrypted_primes[-1]))
        else:
            raise ValueError('Not a valid starting prime')
    return decrypted_primes


def get_first_two_different_prime_products(all_prime_products: List[int]) -> Tuple[int, int]:
    for i in range(len(all_prime_products) - 1):
        if all_prime_products[i] != all_prime_products[i + 1]:
            return all_prime_products[i], all_prime_products[i + 1]


def main():
    cases = int(input())
    for _case in range(cases):
        case_number = _case + 1
        max_prime, number_of_prime_products = list(map(int, input().split()))
        all_prime_products = list(map(int, input().split()))
        if all_prime_products[0] % int(sqrt(all_prime_products[0])) == 0:
            prime_gcd = int(sqrt(all_prime_products[0]))
        else:
            prime_gcd = find_gcd(*get_first_two_different_prime_products(all_prime_products))
        first_prime = prime_gcd
        second_prime = all_prime_products[0] // first_prime
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
