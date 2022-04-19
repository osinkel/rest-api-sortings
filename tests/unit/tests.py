import math
import sys
import unittest
from src.logic.sort_logic import do_sort


class TestSortLogic(unittest.TestCase):

    def test_quick_sort_nums(self):
        res = do_sort('quick', [3,2,4,6,8,4,1,3])
        self.assertListEqual(res['result'], [1,2,3,3,4,4,6,8])
        self.assertNotEqual(res['time'], float('nan'))

    def test_shaker_sort_nums(self):
        res = do_sort('shaker', [3,2,4,6,8,4,1,3])
        self.assertListEqual(res['result'], [1,2,3,3,4,4,6,8])
        self.assertNotEqual(res['time'], float('nan'))

    def test_selection_sort_nums(self):
        res = do_sort('selection', [3,2,4,6,8,4,1,3])
        self.assertListEqual(res['result'], [1,2,3,3,4,4,6,8])
        self.assertNotEqual(res['time'], float('nan'))

    def test_insertion_sort_nums(self):
        res = do_sort('insertion', [3,2,4,6,8,4,1,3])
        self.assertListEqual(res['result'], [1,2,3,3,4,4,6,8])
        self.assertNotEqual(res['time'], float('nan'))

    def test_quick_sort_words(self):
        res = do_sort('quick', ['cow', 'milk', 'dog', 'man', 'article'])
        self.assertListEqual(res['result'],['article', 'cow', 'dog', 'man', 'milk'])
        self.assertNotEqual(res['time'], float('nan'))

    def test_shaker_sort_words(self):
        res = do_sort('shaker', ['cow', 'milk', 'dog', 'man', 'article'])
        self.assertListEqual(res['result'],['article', 'cow', 'dog', 'man', 'milk'])
        self.assertNotEqual(res['time'], float('nan'))

    def test_insertion_sort_words(self):
        res = do_sort('insertion', ['cow', 'milk', 'dog', 'man', 'article'])
        self.assertListEqual(res['result'],['article', 'cow', 'dog', 'man', 'milk'])
        self.assertNotEqual(res['time'], float('nan'))

    def test_selection_sort_words(self):
        res = do_sort('selection', ['cow', 'milk', 'dog', 'man', 'article'])
        self.assertListEqual(res['result'],['article', 'cow', 'dog', 'man', 'milk'])
        self.assertNotEqual(res['time'], float('nan'))

    def test_incorrect_name_sort(self):
        res = do_sort('sdf', [3,2,4,6,8,4,1,3])
        self.assertEqual(res['result'], '')
        self.assertEqual(math.isnan(res['time']), True)

    def test_incorrect_sequence_sort(self):
        res = do_sort('quick', [3, 2, 4, 'dfs', 8, 4, 1, 3])
        self.assertEqual(res['result'], '')
        self.assertEqual(math.isnan(res['time']), True)

    def test_empty_sequence_sort(self):
        res = do_sort('quick', [])
        self.assertEqual(res['result'], '')
        self.assertEqual(math.isnan(res['time']), True)

    def test_not_sequence_sort_int(self):
        res = do_sort('quick', 1)
        self.assertEqual(res['result'], '')
        self.assertEqual(math.isnan(res['time']), True)

    def test_not_sequence_sort_str(self):
        res = do_sort('quick', 'incorrect type')
        self.assertEqual(res['result'], '')
        self.assertEqual(math.isnan(res['time']), True)