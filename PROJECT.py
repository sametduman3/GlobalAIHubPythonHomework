import random

kullanici=input("Lütfen Ad Soyad Giriniz: ")
print("Giriş Başarılı, "+kullanici+" Hoşgeldiniz.")
print("Lütfen Derslerinizi Ekleyiniz..")
derssayisi=0
dersler=[]
while derssayisi < 3:
    dersadi=input("Ders Adı Giriniz: ")
    dersler.append(dersadi)
    derssayisi=derssayisi+1
print("Mevcut Dersleriniz: "+dersler[0]+", "+dersler[1]+", "+dersler[2]+".")
devam=input("Ders Eklemeye Devam Etmek İçin 1'i, Durdurmak için 0'ı Giriniz:  ")
if devam=="1":
    while derssayisi<5:
        dersadi=input("Ders Adı Giriniz: ")
        dersler.append(dersadi)
        derssayisi=derssayisi+1
        
    print("Maksimum Ders Sayısına Ulaştınız.")
    print("Dersleriniz: "+dersler[0]+", "+dersler[1]+", "+dersler[2]+", "+dersler[3]+", "+dersler[4])
    print("Şimdi Notlarını Girme Vakti.")
    
elif devam=="0":
    print("Şimdi Notlarını Girme Vakti.")
    print("İşte Mevcut Derslerin: "+dersler[0]+", "+dersler[1]+", "+dersler[2]+".")
else:
    print("Hatalı bir giriş yaptınız!!!")
vizenotu=input(random.choice(dersler)+ " isimli dersin için VİZE notunu gir: ")
vize=float(vizenotu)
finalnotu=input(random.choice(dersler)+ " isimli dersin için FİNAL notunu gir: ")
final=float(finalnotu)
projenotu=input(random.choice(dersler)+ " isimli dersin için PROJE notunu gir: ")
proje=float(projenotu)
ortalama=((vize*30)/100)+((final*50)/100)+((proje*20)/100)
if ortalama<30:
    print("Harf Notunuz: FF")
    print("BU DERSTEN BAŞARISIZ OLDUNUZ.!!")
elif ortalama>=30 and ortalama<50:
    print("Harf Notunuz: DD")
elif ortalama>=50 and ortalama<70:
    print("Harf Notunuz: CC")
elif ortalama>=70 and ortalama<90:
    print("Harf Notunuz: BB")
elif ortalama>=90 and ortalama<101:
    print("Harf Notunuz: AA")
else:
    print("Hatalı Hesaplama. Lütfen Tekrar Giriş Yapınız.")
    
print("Sayısal Not Ortalaman: "+str(ortalama))
    

    