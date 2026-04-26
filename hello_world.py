def sort_numbers(numbers):
    """Sort a list of numbers in ascending order."""
    return sorted(numbers)


def main():
    print("hello world")

    # Demo sorting function
    numbers = [5, 2, 8, 1, 9, 3]
    sorted_numbers = sort_numbers(numbers)
    print(f"Original: {numbers}")
    print(f"Sorted: {sorted_numbers}")


if __name__ == "__main__":
    main()
