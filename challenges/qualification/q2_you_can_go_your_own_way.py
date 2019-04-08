def reverse_path(path: str) -> str:
    reverse_position = {
        'S': 'E',
        'E': 'S'
    }
    return ''.join([reverse_position[s] for s in path])


def main():
    cases = int(input())
    for _case in range(cases):
        case_number = _case + 1
        _ = input()
        new_path = reverse_path(input())
        print('Case #{case_number}: {new_path}'.format(case_number=case_number, new_path=new_path))


if __name__ == '__main__':
    main()