import unittest
from hello_world import sort_numbers


class TestSortNumbers(unittest.TestCase):
    """Unit tests for the sort_numbers function."""

    def test_sort_basic_list(self):
        """Test sorting a basic unsorted list."""
        result = sort_numbers([5, 2, 8, 1, 9, 3])
        self.assertEqual(result, [1, 2, 3, 5, 8, 9])

    def test_sort_already_sorted(self):
        """Test sorting an already sorted list."""
        result = sort_numbers([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        result = sort_numbers([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_sort_empty_list(self):
        """Test sorting an empty list."""
        result = sort_numbers([])
        self.assertEqual(result, [])

    def test_sort_single_element(self):
        """Test sorting a single element list."""
        result = sort_numbers([42])
        self.assertEqual(result, [42])

    def test_sort_duplicates(self):
        """Test sorting a list with duplicate values."""
        result = sort_numbers([3, 1, 4, 1, 5, 9, 2, 6, 5])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9])

    def test_sort_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        result = sort_numbers([-5, 3, -1, 0, 8, -10])
        self.assertEqual(result, [-10, -5, -1, 0, 3, 8])

    def test_original_list_unchanged(self):
        """Test that the original list is not modified."""
        original = [5, 2, 8, 1, 9, 3]
        original_copy = original.copy()
        sort_numbers(original)
        self.assertEqual(original, original_copy)


if __name__ == "__main__":
    unittest.main()
