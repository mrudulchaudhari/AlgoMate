import unittest
from array_module import ArrayOperations, ArraySearch


class TestArraySearch(unittest.TestCase):
    def setUp(self):
        self.search = ArraySearch()

    def test_linear_search_debug(self):
        self.assertEqual(self.search.linear_search_debug([1, 2, 3], 2), (1, ['Check index 0: 1', 'Check index 1: 2']))
        self.assertEqual(self.search.linear_search_debug([1, 2, 3], 4), (-1, ['Check index 0: 1', 'Check index 1: 2', 'Check index 2: 3']))
        self.assertEqual(self.search.linear_search_debug([], 1), (-1, []))  
        self.assertEqual(self.search.linear_search_debug([5, 3, 8], 5), (0, ['Check index 0: 5']))

    def test_binary_search_debug(self):
        self.assertEqual(self.search.binary_search_debug([1, 2, 3, 4], 3), (2, ['Check middle index 1: 2', 'Check middle index 2: 3']))
        self.assertEqual(self.search.binary_search_debug([1, 2, 3, 4], 5), (-1, ['Check middle index 1: 2', 'Check middle index 2: 3', 'Check middle index 3: 4']))
        self.assertEqual(self.search.binary_search_debug([], 1), (-1, []))  
        self.assertEqual(self.search.binary_search_debug([1, 2, 3, 4], 1), (0, ['Check middle index 1: 2', 'Check middle index 0: 1']))


class TestArrayOperations(unittest.TestCase):
    def setUp(self):
        self.operations = ArrayOperations()

    def test_sum_array(self):
        self.assertEqual(self.operations.sum_array([1, 2, 3]), 6)
        self.assertEqual(self.operations.sum_array([-1, -2, -3]), -6)
        self.assertEqual(self.operations.sum_array([]), 0)
        self.assertEqual(self.operations.sum_array([0]), 0)

    def test_product_array(self):
        self.assertEqual(self.operations.product_array([1, 2, 3]), 6)
        self.assertEqual(self.operations.product_array([-1, -2, -3]), -6)
        self.assertEqual(self.operations.product_array([]), 1)
        self.assertEqual(self.operations.product_array([0]), 0)

    def test_reverse_array(self):
        self.assertEqual(self.operations.reverse_array([1, 2, 3]), [3, 2, 1])
        self.assertEqual(self.operations.reverse_array([]), [])
        self.assertEqual(self.operations.reverse_array([1]), [1])
        self.assertEqual(self.operations.reverse_array([1, 2]), [2, 1])

    def test_rotate_left(self):
        self.assertEqual(self.operations.rotate_left([1, 2, 3], 1), [2, 3, 1])
        self.assertEqual(self.operations.rotate_left([1, 2, 3], 2), [3, 1, 2])
        self.assertEqual(self.operations.rotate_left([1, 2, 3], 3), [1, 2, 3])
        self.assertEqual(self.operations.rotate_left([], 1), [])
        self.assertEqual(self.operations.rotate_left([1], 1), [1])


    def test_rotate_right(self):
        self.assertEqual(self.operations.rotate_right([1, 2, 3], 1), [3, 1, 2])
        self.assertEqual(self.operations.rotate_right([1, 2, 3], 2), [2, 3, 1])
        self.assertEqual(self.operations.rotate_right([1, 2, 3], 3), [1, 2, 3])
        self.assertEqual(self.operations.rotate_right([], 1), [])
        self.assertEqual(self.operations.rotate_right([1], 1), [1])

    def test_remove_duplicates(self):
        self.assertEqual(self.operations.remove_duplicates([1, 2, 2, 3]), [1, 2, 3])
        self.assertEqual(self.operations.remove_duplicates([1, 1, 1]), [1])
        self.assertEqual(self.operations.remove_duplicates([]), [])
        self.assertEqual(self.operations.remove_duplicates([1]), [1])
        self.assertEqual(self.operations.remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_max_min(self):
        self.assertEqual(self.operations.max_min([1, 2, 3]), (3, 1))
        self.assertEqual(self.operations.max_min([-1, -2, -3]), (-1, -3))
        self.assertEqual(self.operations.max_min([]), (None, None))
        self.assertEqual(self.operations.max_min([5]), (5, 5))
        self.assertEqual(self.operations.max_min([1, 2, 3, 4]), (4, 1))

    def test_mean(self):
        self.assertEqual(self.operations.mean([1, 2, 3]), 2.0)
        self.assertEqual(self.operations.mean([-1, -2, -3]), -2.0)
        self.assertEqual(self.operations.mean([]), 0)
        self.assertEqual(self.operations.mean([5]), 5.0)
        self.assertEqual(self.operations.mean([1, 2, 3, 4]), 2.5)

    def test_median(self):
        self.assertEqual(self.operations.median([1, 2, 3]), 2.0)
        self.assertEqual(self.operations.median([1, 2, 3, 4]), 2.5)
        self.assertEqual(self.operations.median([3, 1, 2]), 2.0)
        self.assertEqual(self.operations.median([]), 0)
        self.assertEqual(self.operations.median([5]), 5.0)

    def test_mode(self):
        self.assertEqual(self.operations.mode([1, 2, 2, 3]), 2)
        self.assertEqual(self.operations.mode([1, 1, 2, 2, 3]), [1, 2])
        self.assertEqual(self.operations.mode([]), [])
        self.assertEqual(self.operations.mode([5]), 5)
        self.assertEqual(self.operations.mode([1, 2, 3]), [1, 2, 3])  # No mode, all unique


