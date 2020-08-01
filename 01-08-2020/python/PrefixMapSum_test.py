import PrefixMapSum as p

mapsum = p.PrefixMapSum()

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
