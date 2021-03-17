# EasyDB 

EasyDB, programlarında depoladıkları verileri bir yere kaydetmek isteyen ama bunu anlaşılabilir ve sade bir yolla yapmak isteyen geliştiriciler için tasarladım. Sözlük tipi kullanan bu veritabanı sistemi, kullanması aşırı basit ve büyük verileri depolayabiliyor.

```py
from easydb import EasyDB

veritabani = EasyDB("veritabanim") # Parametreler (dosyaKonum) - Dosya konumu uzantısız şekilde yazılmalı. İsterseniz tam konum verebilirsiniz. Örnek : C:\veritabanim, veritabanlari\veritabanim

# Veritabanına veri ekleme

veritabani.add("isim", "Yusuf") # Parametreler (anahtar, değer) - Değer ekleyebilir veya var olanı değiştirebilirsiniz.
veritabani.add("yas", 15) # Sayı ekleyebilirsiniz.
veritabani.add_dict({"armut":True}) # Bool değer ekleyebilir ve doğrudan Dictionary eklemesi yapabilirsiniz.
veritabani.add("bilgiler", EasyDB("YusufBilgiler")) # Hatta veritabanı içine veritabanı da ekleyebilirsiniz.

# Veritabanından veri okuma

isim = veritabani.get("isim") # Parametreler (anahtar) - Eğer bu anahtar varsa değerini döndürür. Yoksa None döndürür. 
yas = veritabani.get("yas")
bilgiler = veritabani.get("bilgiler")

print("İsim : {} - Yaş : {} - Bilgiler : {}".format(isim, yas, bilgiler)) # Çıktı : "İsim : Yusuf - Yaş : 15 - Bilgiler : <easydb.EasyDB object at 0xfffffffffffffffffff>"

# Veritabanının objesine erişme

veritabani_obje = veritabani.object()
bilgiler_obje = veritabani.get("bilgiler").object()

veritabani.get("bilgiler").add("boy",170) # Çıktılarken boş çıkmaması için bir değer ekleyelim.

print("Veritabani : {} -  Bilgi Veritabani : {}".format(veritabani_obje, bilgiler_obje)) # Çıktı : "Veritabani : {'isim':'Yusuf', 'yas':15, 'armut': True, bilgiler:<easydb.EasyDB object at 0xfffffffffffffffffff>} -  Bilgi Veritabani : {'boy':150}"

# Veritabanından veri silme

veritabani.delete("isim")
print(veritabani.object()) # Çıktı : {'yas':15, 'armut': True, bilgiler:<easydb.EasyDB object at 0xfffffffffffffffffff>}

# RAM Üzerinde veritabanı çalıştırma

ram_veritabani = EasyDB(":memory:") # Konum kısmına :memory: yazarsanız veritabanı RAM'de çalışır ve değişiklikler diske kaydedilmez.

ram_veritabani.add("test",123)
print(ram_veritabani.object()) # Çıktı : {'test': 123}
```
