"""Binary Search Tree — ekleme + ağacı yan yatmış şekilde çizme.

Çalıştır:  python3 kodlar/bst.py
"""


class Dugum:
    def __init__(self, deger):
        self.deger, self.sol, self.sag = deger, None, None


def ekle(kok, deger):
    if kok is None:
        return Dugum(deger)
    if deger < kok.deger:
        kok.sol = ekle(kok.sol, deger)
    else:
        kok.sag = ekle(kok.sag, deger)
    return kok


def inorder(kok):
    return inorder(kok.sol) + [kok.deger] + inorder(kok.sag) if kok else []


def ciz(kok, girinti=0):
    """Sağ alt ağaç üstte, sol alt ağaç altta (90° sola yatırılmış ağaç)."""
    if kok:
        ciz(kok.sag, girinti + 4)
        print(" " * girinti + str(kok.deger))
        ciz(kok.sol, girinti + 4)


if __name__ == "__main__":
    kok = None
    for x in [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]:
        kok = ekle(kok, x)
    ciz(kok)
    print("\nInorder (sıralı olmalı):", inorder(kok))
