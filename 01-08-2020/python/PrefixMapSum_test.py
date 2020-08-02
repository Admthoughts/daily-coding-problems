import PrefixMapSum as p
import unittest

class Test_PrefixMapSum(unittest.TestCase):
    
    def test_MapSum_Insert(self):
        mapsum = p.PrefixMapSum()
        want = {"columnar": 3}
        mapsum.insert("columnar",3)
        self.assertEqual(mapsum.keymap, want)
        mapsum.insert("columnar",3)
        self.assertEqual(mapsum.keymap, want)

    def test_MapSum_Sum(self):
        mapsum = p.PrefixMapSum()
        mapsum.keymap = {"columnar": 3, "column": 2,}
        want = 5
        self.assertEqual(mapsum.sum("col"), want)

# mapsum.insert("columnar", 3)
# assert mapsum.sum("col") == 3

# mapsum.insert("column", 2)
# assert mapsum.sum("col") == 5

if __name__ == '__main__':
    unittest.main()