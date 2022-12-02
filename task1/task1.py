def check_continue() -> bool:
    return validate_continue(input('Do you want to add more numbers? [d/n] '))


def validate_continue(s: str) -> bool:
    return not s.lower().startswith('n')


def gather_numbers() -> list[float]:
    numbers: list[float] = []
    cont: bool = True
    while cont:
        x: str = input('Next number: ')
        try:
            numbers.append(float(x))
        except ValueError:
            print(f'The value {x} could not be interpreted as a number')
        cont = check_continue()
    return numbers


def convert_to_int(x: float) -> float | int:
    if x.is_integer():
        return int(x)
    return x


def get_longest_increasing_subsequence(numbers: list[float]) -> list[float]:
    subsequences = []
    if not numbers:
        return []
    for num in numbers:
        used = False
        for subseq in subsequences:
            if num > subseq[-1]:
                subsequences.append([*subseq, num])
                used = True
        if not used:
            subsequences.append([num])
    subsequences = sorted(subsequences, key=lambda subseq: len(subseq), reverse=True)
    return [convert_to_int(x) for x in subsequences[0]]


def get_longest_decreasing_subsequence(numbers: list[float]) -> list[float]:
    inverted_numbers = [-x for x in numbers]
    longest_subsequence = get_longest_increasing_subsequence(inverted_numbers)
    return [-x for x in longest_subsequence]


def get_longest_monotone_subsequence(numbers: list[float]) -> list[float]:
    longest_increasing: list[float] = get_longest_increasing_subsequence(numbers)
    longest_decreasing = get_longest_decreasing_subsequence(numbers)
    if len(longest_increasing) > len(longest_decreasing):
        return longest_increasing
    return longest_decreasing


def get_sum(numbers: list[float]) -> float | int:
    s: float = sum(numbers)
    if s.is_integer():
        return int(s)
    return s


def main() -> None:
    numbers: list[float] = gather_numbers()
    print(f'The sum is equal to {get_sum(numbers)}')
    print(f'The longest increasing subsequence is {get_longest_increasing_subsequence(numbers)}')
    print(f'The longest monotone subsequence is {get_longest_monotone_subsequence(numbers)}')


if __name__ == '__main__':
    main()
