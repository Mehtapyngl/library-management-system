from abc import ABC, abstractmethod



class Kaynak(ABC):
    
    def __init__(self, baslik: str, kayitNo: int):
        # Kapsülleme (Encapsulation) kuralları gereği özellikler __ ile gizlendi
        self.__baslik = baslik
        self.__kayitNo = kayitNo

    # --- Kapsüllenmiş Değişkenler İçin Getter ve Setter Metotları ---
    @property
    def baslik(self):
        return self.__baslik

    @baslik.setter
    def baslik(self, yeni_baslik):
        if yeni_baslik.strip(): # Boş bırakılmasını engellemek için kontrol
            self.__baslik = yeni_baslik

    @property
    def kayitNo(self):
        return self.__kayitNo

    @kayitNo.setter
    def kayitNo(self, yeni_kayitNo):
        if yeni_kayitNo > 0:
            self.__kayitNo = yeni_kayitNo

    @abstractmethod
    def __str__(self):
       
        pass


class Kitap(Kaynak):
    
    def __init__(self, baslik: str, kayitNo: int, yazar: str, sayfaSayisi: int):
        # Üst sınıfın (Kaynak) yapıcı metodunu çağırma
        super().__init__(baslik, kayitNo)
        # Kitaba özel eklenen 2 yeni özellik
        self.__yazar = yazar
        self.__sayfaSayisi = sayfaSayisi

    @property
    def yazar(self): return self.__yazar

    @property
    def sayfaSayisi(self): return self.__sayfaSayisi

    def __str__(self):
        return f"[KİTAP] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Yazar: {self.yazar} | Sayfa: {self.sayfaSayisi}"


class Dergi(Kaynak):
    
    def __init__(self, baslik: str, kayitNo: int, yayinDonemi: str, sayiNo: int):
        super().__init__(baslik, kayitNo)
        # Dergiye özel eklenen 2 yeni özellik
        self.__yayinDonemi = yayinDonemi
        self.__sayiNo = sayiNo

    @property
    def yayinDonemi(self): return self.__yayinDonemi

    @property
    def sayiNo(self): return self.__sayiNo

    def __str__(self):
        return f"[DERGİ] Kayıt No: {self.kayitNo} | Başlık: {self.baslik} | Dönem: {self.yayinDonemi} | Sayı No: {self.sayiNo}"




class Islem(ABC):
   
    @abstractmethod
    def ekle(self): pass

    @abstractmethod
    def sil(self): pass

    @abstractmethod
    def guncelle(self): pass

    @abstractmethod
    def listele(self): pass


class KitapIslem(Islem):
    def __init__(self):
        self.kitaplar = []

    def ekle(self):
        print("\n--- Yeni Kitap Ekle ---")
        try:
            kayit_no = int(input("Kayıt No (Sayı): "))
            baslik = input("Kitap Adı: ")
            yazar = input("Yazar Adı: ")
            sayfa = int(input("Sayfa Sayısı (Sayı): "))
            
            yeni_kitap = Kitap(baslik, kayit_no, yazar, sayfa)
            self.kitaplar.append(yeni_kitap)
            print("✔️ Kitap başarıyla kütüphaneye eklendi.")
        except ValueError:
            print("❌ Hata: Kayıt No ve Sayfa Sayısı sayısal bir değer olmalıdır!")

    def sil(self):
        print("\n--- Kitap Sil ---")
        try:
            k_no = int(input("Silmek istediğiniz kitabın Kayıt No'sunu girin: "))
            for kitap in self.kitaplar:
                if kitap.kayitNo == k_no:
                    self.kitaplar.remove(kitap)
                    print(f"✔️ {kitap.baslik} adlı kitap başarıyla silindi.")
                    return
            print("❌ Belirtilen Kayıt No ile bir kitap bulunamadı.")
        except ValueError:
            print("❌ Hata: Geçersiz kayıt numarası.")

    def guncelle(self):
        print("\n--- Kitap Güncelle ---")
        try:
            k_no = int(input("Güncellemek istediğiniz kitabın Kayıt No'sunu girin: "))
            for kitap in self.kitaplar:
                if kitap.kayitNo == k_no:
                    yeni_baslik = input(f"Yeni Başlık (Eski: {kitap.baslik}): ")
                    if yeni_baslik: kitap.baslik = yeni_baslik
                    print("✔️ Kitap bilgileri güncellendi.")
                    return
            print("❌ Kitap bulunamadı.")
        except ValueError:
            print("❌ Hata: Geçersiz giriş.")

    def listele(self):
        print("\n--- Kitap Listesi ---")
        if not self.kitaplar:
            print("Kütüphanede kayıtlı kitap bulunmuyor.")
        else:
            for kitap in self.kitaplar:
                print(kitap)


class DergiIslem(Islem):
    def __init__(self):
        self.dergiler = []

    def ekle(self):
        print("\n--- Yeni Dergi Ekle ---")
        try:
            kayit_no = int(input("Kayıt No (Sayı): "))
            baslik = input("Dergi Adı: ")
            donem = input("Yayın Dönemi (Aylık/Haftalık): ")
            sayi = int(input("Sayı No (Sayı): "))
            
            yeni_dergi = Dergi(baslik, kayit_no, donem, sayi)
            self.dergiler.append(yeni_dergi)
            print("✔️ Dergi başarıyla kütüphaneye eklendi.")
        except ValueError:
            print("❌ Hata: Sayısal alanları kontrol edin!")

    def sil(self):
        print("\n--- Dergi Sil ---")
        try:
            k_no = int(input("Silmek istediğiniz derginir Kayıt No'sunu girin: "))
            for dergi in self.dergiler:
                if dergi.kayitNo == k_no:
                    self.dergiler.remove(dergi)
                    print(f"✔️ {dergi.baslik} adlı dergi başarıyla silindi.")
                    return
            print("❌ Dergi bulunamadı.")
        except ValueError:
            print("❌ Hata: Geçersiz kayıt numarası.")

    def guncelle(self):
        print("\n--- Dergi Güncelle ---")
        try:
            k_no = int(input("Güncellemek istediğiniz derginin Kayıt No'sunu girin: "))
            for dergi in self.dergiler:
                if dergi.kayitNo == k_no:
                    yeni_baslik = input(f"Yeni Başlık (Eski: {dergi.baslik}): ")
                    if yeni_baslik: dergi.baslik = yeni_baslik
                    print("✔️ Dergi bilgileri güncellendi.")
                    return
            print("❌ Dergi bulunamadı.")
        except ValueError:
            print("❌ Hata: Geçersiz giriş.")

    def listele(self):
        print("\n--- Dergi Listesi ---")
        if not self.dergiler:
            print("Kütüphanede kayıtlı dergi bulunmuyor.")
        else:
            for dergi in self.dergiler:
                print(dergi)




def ana_menu():
    kitap_sistemi = KitapIslem()
    dergi_sistemi = DergiIslem()

    while True:
        # İpuçlarındaki toplam kayıt göstergesi (Bonus özellik)
        toplam_kayit = len(kitap_sistemi.kitaplar) + len(dergi_sistemi.dergiler)
        
        print("\n*************************************************")
        print("           KÜTÜPHANE YÖNETİM SİSTEMİ             ")
        print(f"           (Sistemdeki Toplam Kayıt: {toplam_kayit})")
        print("*************************************************")
        print("  1 - Kitap Ekle")
        print("  2 - Kitap Sil")
        print("  3 - Kitap Güncelle")
        print("  4 - Kitapları Listele")
        print("  5 - Dergi Ekle")
        print("  6 - Dergi Sil")
        print("  7 - Dergi Güncelle")
        print("  8 - Dergileri Listele")
        print("  9 - Çıkış")
        print("*************************************************")
        
        secim = input("Seçiminiz (1-9): ")
        
        if secim == "1":
            kitap_sistemi.ekle()
        elif secim == "2":
            kitap_sistemi.sil()
        elif secim == "3":
            kitap_sistemi.guncelle()
        elif secim == "4":
            kitap_sistemi.listele()
        elif secim == "5":
            dergi_sistemi.ekle()
        elif secim == "6":
            dergi_sistemi.sil()
        elif secim == "7":
            dergi_sistemi.guncelle()
        elif secim == "8":
            dergi_sistemi.listele()
        elif secim == "9":
            print("\nSistemden çıkış yapılıyor... İyi günler!")
            break
        else:
            print("❌ Geçersiz seçim! Lütfen 1-9 arasında bir değer girin.")

# Programı Başlatma
if __name__ == "__main__":
    ana_menu()
