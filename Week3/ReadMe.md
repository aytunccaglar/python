## **HW1** ##
```python
def rvs(kelime):
    harfler = []
    for i in range(len(kelime)):
        harfler.append(kelime[i])
    for j in range(int(len(harfler) / 2)):
        harfler[j], harfler[len(harfler) - 1 - j] = harfler[len(harfler) - 1 - j], harfler[j]
    return harfler


var = input("kelime veya cümle gir:")
print(rvs(var))
```
> Açıklama:
İlk önce fonksiyon oluşturdum.Harfler dizisi oluşturdum.İlk döngüde İ'yi girilen kelime kadar döngüye alıyor ve diziye atıyor.
Sonra J döngüsü ile harfleri yarısı kadar döngüye alıyor.Yer değiştirme işlemi yapıp harflere döndürüyor ve yazdırıyor.
