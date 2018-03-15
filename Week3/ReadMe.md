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
İLK ÖNCE FONKSİYON OLUŞTURDUM.HARFLER DİZİ OLUŞTURDUM.İLK DÖNGÜDE İ'Yİ GİRİLEN KELİME KADAR DÖNGÜYE ALIYOR VE DİZİYE ATIYOR.
SONRA J DÖNGÜSÜ İLE HARFLERİ YARISI KADAR DÖNGÜYE ALIYOR.YER DEĞİŞTİRME İŞLEMİNİ YAPIP HARFLERE DÖNDÜRÜYOR.VE YAZDIRIYOR
