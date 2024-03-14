import unittest
from dict2 import dict2, DictKeyNotFoundError

class TestDict2(unittest.TestCase):
    def test_store_and_access_values(self):
        obj = dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3

        self.assertEqual(obj['a'], 1)
        self.assertEqual(obj['b'], 2)
        self.assertEqual(obj['c'], 3)

    def test_custom_exception(self):
        obj = dict2()

        with self.assertRaises(DictKeyNotFoundError):
            val = obj['a']

    def test_iteration_through_keys(self):
        obj = dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3

        keys = []
        for k in obj:
            keys.append(k)

        self.assertListEqual(keys, ['a', 'b', 'c'])

    def test_update_existing_key(self):
        obj = dict2()
        obj['a'] = 1
        obj['b'] = 2
        obj['c'] = 3
        obj['a'] = 4

        self.assertEqual(obj['a'], 4)

if __name__ == '__main__':
    unittest.main()
