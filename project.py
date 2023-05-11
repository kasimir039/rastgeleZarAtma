import random


zarSayisi = 6
tahminler = []
zarlar = []

for i in range(zarSayisi):
    zarlar.append(random.randint(1,6))
 
for i in range(zarSayisi):
    tahmin = int(input("{} zarın tahmini".format(i+1)))
    tahminler.append(tahmin)
    while True:
        if tahmin > 6:
            print("Sayı 6 dan büyük olamaz!")
            tahmin = int(input("{} zarın tahmini".format(i+1)))
        else:
            break

print("\nAtılan Zarlar")
print(tahminler)

print("\nRastgele Atılan Zarlar")
print(zarlar)
        
