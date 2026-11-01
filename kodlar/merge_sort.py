"""Merge Sort — böl, sırala, birleştir. Her birleştirmeyi basar.

Çalıştır:  python3 kodlar/merge_sort.py
"""


def merge_sort(a, iz=False, derinlik=0):
    if len(a) <= 1:
        return list(a)
    orta = len(a) // 2
    sol = merge_sort(a[:orta], iz, derinlik + 1)
    sag = merge_sort(a[orta:], iz, derinlik + 1)
    sonuc, i, j = [], 0, 0
    while i < len(sol) and j < len(sag):
        if sol[i] <= sag[j]:
            sonuc.append(sol[i]); i += 1
        else:
            sonuc.append(sag[j]); j += 1
    sonuc += sol[i:] + sag[j:]
    if iz:
        print("  " * derinlik + f"birleştir {sol} + {sag} -> {sonuc}")
    return sonuc


if __name__ == "__main__":
    print("Ödev: [16,21,11,8,12,22]")
    print("Sonuç:", merge_sort([16, 21, 11, 8, 12, 22], iz=True))
