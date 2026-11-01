"""Notlardaki elle yazılmış cevapları koda karşı doğrular.

Çalıştır:  python3 kodlar/test_notlar.py
"""
import random

from bst import ekle, inorder
from insertion_sort import insertion_sort
from merge_sort import merge_sort

# 1) Rastgele dizilerde Python'un sorted() ile karşılaştır
for _ in range(500):
    d = [random.randint(-50, 50) for _ in range(random.randint(0, 20))]
    assert insertion_sort(d) == sorted(d)
    assert merge_sort(d) == sorted(d)
    kok = None
    for x in d:
        kok = ekle(kok, x)
    assert inorder(kok) == sorted(d)

# 2) Notlardaki somut cevaplar
assert insertion_sort([22, 27, 16, 2, 18, 6]) == [2, 6, 16, 18, 22, 27]
assert merge_sort([16, 21, 11, 8, 12, 22]) == [8, 11, 12, 16, 21, 22]

kok = None
for x in [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]:
    kok = ekle(kok, x)
assert kok.deger == 7
assert (kok.sol.deger, kok.sag.deger) == (5, 8)
assert (kok.sol.sol.deger, kok.sol.sag.deger) == (1, 6)
assert kok.sol.sol.sag.sol.deger == 2 and kok.sol.sol.sag.sag.deger == 4

print("Tüm testler geçti ✓")
