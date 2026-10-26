import socket
import datetime
import sys

# Başlık Ekranı
print("=" * 60)
print("     GÖNEN MYO BİLİŞİM GÜVENLİĞİ - PORT TARAYICI & RAPORLAYICI")
print("=" * 60)

# Kullanıcıdan Hedef Alma
hedef_input = input("\nTaranacak Hedef IP veya Domain adresi girin: ")

try:
    hedef_ip = socket.gethostbyname(hedef_input)
except socket.gaierror:
    print("\n[!] Hata: Domain adı veya IP adresi çözümlenemedi!")
    sys.exit()

print(f"\n[*] Hedef IP: {hedef_ip}")
print(f"[*] Tarama Başlangıcı: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-" * 60)

# Kritik Portlar ve Servis Açıklamaları
KRITIK_PORTLAR = {
    21: "FTP (Dosya Transferi - Şifresiz Veri Aksı Riski)",
    22: "SSH (Guvenli Kabuk - Brute Force Saldırı Hedefi)",
    23: "TELNET (Eski Güvensiz Metin Protokolü)",
    25: "SMTP (E-Posta Sunucusu)",
    53: "DNS (Alan Adı Servisi)",
    80: "HTTP (Web Sunucusu - Şifrelenmemiş Bağlantı)",
    110: "POP3 (E-Posta Servisi)",
    443: "HTTPS (Güvenli Web Sunucusu)",
    3306: "MySQL (Veritabanı Servisi)",
    3389: "RDP (Windows Uzak Masaüstü - Yüksek Risk)"
}

acik_portlar = []

# "a" (append) modu sayesinde eski silinmez, alt alta eklenir.
with open("tarama_raporu.txt", "a", encoding="utf-8") as rapor:
    # Her yeni tarama için üst üste karışmasın diye ayıraç koyuyoruz
    rapor.write("\n" + "=" * 50 + "\n")
    rapor.write("          YENİ TARAMA OTURUMU RAPORU             \n")
    rapor.write("=" * 50 + "\n")
    rapor.write(f"Hedef Girdi: {hedef_input}\n")
    rapor.write(f"Hedef IP   : {hedef_ip}\n")
    rapor.write(f"Tarih      : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    rapor.write("-" * 50 + "\n\n")

    print("[*] Portlar taranıyor, lütfen bekleyin...\n")

    for port, servis in KRITIK_PORTLAR.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)

        sonuc = s.connect_ex((hedef_ip, port))

        if sonuc == 0:
            satir = f"[+] PORT AÇIK: {port:<5} | Servis: {servis}"
            print(satir)
            rapor.write(satir + "\n")
            acik_portlar.append((port, servis))
        s.close()

    rapor.write("\n--------------------------------------------------\n")
    rapor.write(f"ÖZET: Toplam {len(acik_portlar)} adet açık port tespit edildi.\n")

print("-" * 60)
print(f"\n[✓] Tarama tamamlandı! Toplam {len(acik_portlar)} açık port bulundu.")
print("[✓] Sonuçlar 'tarama_raporu.txt' dosyasına alt alta eklendi.\n")
