"""Insertion Sort — en küçük haliyle, adım adım iz (trace) basarak.

Çalıştır:  python3 kodlar/insertion_sort.py
"""


def insertion_sort(dizi, iz=False):
    a = list(dizi)
    for i in range(1, len(a)):
        anahtar = a[i]
        j = i - 1
        while j >= 0 and a[j] > anahtar:  # büyükleri bir sağa kaydır
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = anahtar
        if iz:
            print(f"{i}. adım ({anahtar} yerleşti): {a}")
    return a


if __name__ == "__main__":
    print("Ödev 1: [22,27,16,2,18,6]")
    insertion_sort([22, 27, 16, 2, 18, 6], iz=True)
    print("\nÖdev 2 (ilk 4 adım): [7,3,5,8,2,9,4,15,6]")
    insertion_sort([7, 3, 5, 8, 2, 9, 4, 15, 6], iz=True)
