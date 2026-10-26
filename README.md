# 🛡️ Python TCP Port Scanner & Automated Reporter

Selam! 👋 Bu proje, Balıkesir Üniversitesi Gönen MYO Bilişim Güvenliği Teknolojisi öğrencisi olarak, teoride öğrendiklerimi **pratiğe dökmek** ve sıfırdan kendi güvenlik aracımı yazmak amacıyla geliştirdiğim pratik bir keşif (recon) scriptidir. 

Siber güvenlikte en önemli kuralın başkalarının araçlarını körü körüne ezberlemek değil, arka planda ne çalıştığını anlamak olduğunun bilinciyle bu projeyi adım adım kurguladık.

---

## 🚀 Bu Araç Ne Yapıyor?
* **TCP Soket Mantığı:** Karmaşık ve şişirilmiş kütüphanelere boğulmadan, Python'ın kendi doğasında var olan `socket` modülüyle hedef IP üzerindeki kritik portlara doğrudan TCP bağlantı testi yapar.
* **Düzenli ve Kalıcı Raporlama:** Taranan sonuçları her seferinde silmek yerine, `tarama_raporu.txt` dosyasına aralarına şık çizgiler atarak alt alta kaydeder. Böylece geçmiş tüm tarama oturumlarını tek bir yerden takip edebilirsin.
* **Lab & TryHackMe Uyumlu:** İster internet üzerindeki yasal test adreslerini (`scanme.nmap.org`), ister kendi kurduğun sanal makineleri, isterse de TryHackMe VPN lab ortamındaki zafiyetli makineleri güvenle tarayabilirsin.

---

## 🛠️ Hangi Teknolojileri Kullandık?
* **Programlama Dili:** Python 3
* **Yerleşik Kütüphaneler:** `socket`, `datetime`, `sys` (Ekstra modül kurma derdi yok, tamamen saf ve hızlı!)
* **İşletim Sistemi / Ortam:** Kali Linux

---

## ⚙️ Nasıl Çalıştırırsın?

Kodu kendi ortamında test etmek istersen izleyeceğin adımlar çok basit:

1. Depoyu klonla:
   ```bash
   git clone [https://github.com/esmossgr/python-port-scanner.git]
