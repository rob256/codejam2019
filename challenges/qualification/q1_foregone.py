from typing import Tuple


def split_numbers_without_4(number_to_split: int) -> Tuple[int, int]:
    x = 0

    original_number_to_split = number_to_split
    second_number = 0

    while number_to_split > 0:
        last_number = number_to_split % 10
        if last_number == 4:
            second_number += 10 ** x
        number_to_split //= 10
        x += 1

    return original_number_to_split - second_number, second_number


def main():
    cases = int(input())
    for _case in range(cases):
        case_number = _case + 1
        num1, num2 = split_numbers_without_4(int(input()))
        print('Case #{case_number} {num1} {num2}'.format(case_number=case_number, num1=num1, num2=num2))


if __name__ == '__main__':
    main()
