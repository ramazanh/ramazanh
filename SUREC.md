# Öğrenme Süreci: Karpathy Döngüsü

Kaynak: [@DmitroCP — "The Karpathy Playbook"](https://x.com/dmitrocp/status/2114303402083856499)

## Yazının özü

Karpathy'nin kariyerindeki unvanlar (OpenAI, Tesla) sonuçtu; asıl motor **öğretmek**ti:
karmaşık bir şeyi alıp **sıfırdan, olabildiğince az kodla yeniden yazmak** ve bunu bir yabancının
takip edebileceği netlikte anlatmak (CS231n, char-rnn, micrograd → nanoGPT → nanochat).

```
Makaleyi oku       → kelimeleri bilirsin
Kodla              → mekaniği bilirsin
Birine öğret       → neyin önemli olduğunu bilirsin
```

**Eleştirel not:** Yazı bir başarı hikâyesi; Karpathy'nin Toronto/Stanford/Hinton–Fei-Fei Li çevresi
herkesin kopyalayabileceği bir şey değil. Ama döngünün kendisi ünlü bir işveren gerektirmiyor —
bu repo için kopyalanabilir kısım tam olarak o.

## Bu repoya uyarlanmış döngü

Her konu (algoritma / veri yapısı) şu 5 adımdan geçer:

| # | Adım | Bu repoda karşılığı |
|---|------|---------------------|
| 1 | **Konu seç** — her gün kullandığın ama anlatamadığın bir şey | Ödev konusu (ör. Insertion Sort) |
| 2 | **Elle çöz** | Kök dizindeki not dosyası (`instertation_order`, `Merge_Sort`, …) |
| 3 | **En küçük haliyle sıfırdan kodla** | `kodlar/<konu>.py` — kütüphane yok, ~30 satır, adım adım `iz` basar |
| 4 | **Doğrula** — elle yazdığın cevabı koda karşı test et | `kodlar/test_notlar.py` |
| 5 | **Anlat ve adlandır** — boş ekrandan sesli anlat, şaşırtan kısmı tek cümleyle yaz | Not dosyasının sonuna "Öğrendiğim" bölümü |

Kural: *Çalıştırması 5 dakikadan uzun süren şey ezberde kalmaz.* Her dosya tek komutla çalışır:

```bash
cd kodlar
python3 test_notlar.py      # tüm notları doğrula
python3 insertion_sort.py   # adım adım iz
python3 merge_sort.py
python3 bst.py
python3 selection_bubble.py
```

## Döngünün ilk turu — mevcut notlarda bulunanlar

Kodu yazıp çalıştırmak, notlardaki şu noktaları ortaya çıkardı (4. adımın neden önemli olduğunun kanıtı):

- **Insertion Sort — Best/Worst/Average case açıklaması yanlış kavramla yazılmış.**
  Notta "aradığımız sayının başta/ortada/sonda olması" deniyor; bu *arama* (linear search) dili.
  Sıralamada doğrusu:
  - Best case **O(n)**: dizi zaten sıralı (her eleman tek karşılaştırmayla yerinde kalır).
  - Worst case **O(n²)**: dizi ters sıralı (her eleman en başa kadar kayar).
  - Average case **O(n²)**: rastgele dizi.
- **"O(n²) → 6² = 36"** ifadesi yanıltıcı: Big-O tam adım sayısı vermez, büyüme hızını verir.
  6 elemanlı dizide en kötü durumda gerçek karşılaştırma sayısı n(n−1)/2 = 15'tir.
- **Insertion Sort adımları** (her iki ödev) ve **BST çizimi** kodla birebir doğrulandı ✓
- **Merge Sort:** sonuç doğru ✓. Not, tek sayılı yarıyı `16,21 | 11` diye bölmüş; kod `16 | 21,11`
  bölüyor (`orta = len // 2`). İkisi de geçerli — sınavda hangi kuralı kullandığını belirt.

## Sıradaki konular (her biri bir tur)

- [x] Selection Sort / Bubble Sort — karşılaştırma sayısını sayan sayaç ekle (`Selection_Bubble_Sort`, `kodlar/selection_bubble.py`)
- [ ] Quick Sort — pivot seçiminin worst case'e etkisi
- [ ] Binary Search — BST ile ilişkisi
- [ ] BST silme (3 durum: yaprak, tek çocuk, iki çocuk)
- [ ] Heap / Priority Queue
- [ ] Hash Table — çakışma çözümü

Her turun sonunda: kod + test + "Öğrendiğim" cümlesi aynı commit'te.
