name=input("Lutfen İsminizi Giriniz: ")
surname=input("Lutfen Soy isminizi Giriniz: ")
age=input("Lutfen Yasinizi Giriniz: ")
age1=int(age)
list1=["Ad: "+name,"Soyad: "+surname,"Yaş: "+age]
print("******** KULLANICI BİLGİLERİ **************")
for veri in list1:
   print (veri)
print("Yaşınız Kontrol Ediliyor........")
if age1<0 or age1>90:
    print("Geçersiz Yaş Aralığı...")
elif age1<18:
    print("Yaşınız 18'den Küçük Lütfen Çıkış Yapınız.")
elif age1>18 :
    print("Yaşınız İstenilen Aralıklardadır. İyi Forumlar.")
else:
    print( "Hatalı Giriş Yaptınız...")
print("                                                                                        SametDUMAN#2020")