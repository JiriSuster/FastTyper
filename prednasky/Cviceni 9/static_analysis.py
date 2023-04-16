"""Module providingFunction random."""
import random

def get_random_numbers(count):
    """return random number in amount we provide in count"""
    random_numbers = []
    for _ in range(count):
        random_numbers.append(random.randint(1, 100))
    return random_numbers


def bubble_sort(numbers):
    """order list of value with buble sort"""
    numbers_len = len(numbers)
    for i in range(numbers_len):
        for j in range(0, numbers_len - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


COUNT = 10
random_num = get_random_numbers(COUNT)
sorted_num = bubble_sort(random_num)
print(f"Random numbers: {random_num}")
print(f"Sorted numbers: {sorted_num}")


# python -m pylint .\static_analysis.py
# python -m isort .\static_analysis.py
# python -m black .\static_analysis.py
