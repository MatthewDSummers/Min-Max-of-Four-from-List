"""
    Given a list of positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the integers.
    Then print the respective minimum and maximum values as a single line of two space-separated integers.

    Constraints: 1 <= arr[i] <= 10^9
"""

def min_max_of_four_from_list(arr):
    if failed_contraints(arr):
        return

    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[-4:])

    print(min_sum, max_sum)

def failed_contraints(arr):
    if len(arr) < 4:
        print("List should have at least 4 items")
        return True

    failures = sum(1 for num in arr if num < 1 or num > 10**9)
    if failures != 0:
        print("Items should be greater than 0 and less than 1 billion")
        return True

    return False

if __name__ == '__main__':
    try:
        arr = list(map(int, input("Provide space-separated positive integers--each less than 1 billion\n").rstrip().split()))
        min_max_of_four_from_list(arr)
    except ValueError:
        print("Please provide at least 4 space-separated positive integers--each less than 1 billion")
