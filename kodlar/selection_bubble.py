"""Selection Sort ve Bubble Sort — karşılaştırma ve takas sayaçlarıyla.

Çalıştır:  python3 kodlar/selection_bubble.py
"""


def selection_sort(dizi, iz=False):
    a, karsilastirma, takas = list(dizi), 0, 0
    for i in range(len(a) - 1):
        en_kucuk = i
        for j in range(i + 1, len(a)):  # kalan kısımdaki en küçüğü bul
            karsilastirma += 1
            if a[j] < a[en_kucuk]:
                en_kucuk = j
        if en_kucuk != i:
            a[i], a[en_kucuk] = a[en_kucuk], a[i]
            takas += 1
        if iz:
            print(f"{i + 1}. tur: {a}")
    return a, karsilastirma, takas


def bubble_sort(dizi, iz=False):
    a, karsilastirma, takas = list(dizi), 0, 0
    n = len(a)
    for tur in range(n - 1):
        degisti = False
        for j in range(n - 1 - tur):  # en büyük sona "kabarcıklanır"
            karsilastirma += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                takas += 1
                degisti = True
        if iz:
            print(f"{tur + 1}. tur: {a}")
        if not degisti:  # erken çıkış: best case O(n)
            break
    return a, karsilastirma, takas


if __name__ == "__main__":
    ornek = [29, 10, 14, 37, 13]
    for ad, f in [("Selection", selection_sort), ("Bubble", bubble_sort)]:
        print(f"\n{ad} Sort: {ornek}")
        _, k, t = f(ornek, iz=True)
        print(f"-> {k} karşılaştırma, {t} takas")

    print("\nKarşılaştırma sayıları (n=6):")
    for durum, d in [("sıralı", [1, 2, 3, 4, 5, 6]), ("ters", [6, 5, 4, 3, 2, 1])]:
        print(f"  {durum:7} selection={selection_sort(d)[1]:2}  bubble={bubble_sort(d)[1]:2}")
