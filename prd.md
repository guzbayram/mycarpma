Ürün Gereksinimleri Belgesi (PRD): Çarpım Tablosu Öğrenme Uygulaması


1. Ürün Amaç ve Kapsamı

Amaç: İlkokul öğrencilerine çarpım tablosunu eğlenceli ve etkili bir şekilde öğretmek, Çin yöntemiyle köşegenin üst kısmına odaklanarak zamandan tasarruf sağlamak, zorlanılan soruları Anki algoritmasıyla tekrar ettirmek.
Hedef Kitle: 7-10 yaş arası ilkokul öğrencileri ve ebeveynler.
Platform: Web (Django) + Mobil Uyumlu (Responsive Tasarım).

2. Temel Özellikler

Çin Yöntemi Odaklı Soru Havuzu:
Köşegenin üst kısmındaki çarpımlar (örneğin, 2x3 ama 3x2 sorulmaz).
Sıfır (0xN), bir (1xN), beş (5xN) ve on (10xN) ile çarpma soruları çıkarılır.
Anki Tarzı Tekrar Sistemi:
Kullanıcının yanlış cevapladığı sorular daha sık tekrar edilir.
Doğru cevaplanan soruların tekrar aralığı artar.
Eğlenceli Arayüz:
Renkli animasyonlar, başarı rozetleri ve sesli geri bildirim.
Çocuk dostu karakterler ve ödül sistemi (yıldızlar, kupalar).
Kullanıcı Profili ve İlerleme Takibi:
Ebeveynlerin çocuğun ilerlemesini görebileceği bir panel.
Haftalık raporlar (doğru/yanlış oranı, en çok zorlanılan çarpmalar).
Mobil Uyumluluk:
Tüm ekran boyutlarına uyumlu responsive tasarım.
3. Teknik Gereksinimler

Backend:
Django ile kullanıcı kimlik doğrulama, soru havuzu yönetimi ve Anki algoritması.
Veritabanı: PostgreSQL veya SQLite (soru-cevap logları ve kullanıcı verileri).
Frontend:
Bootstrap veya Tailwind CSS ile responsive tasarım.
JavaScript ile interaktif soru-cevap mekanizması.
Algoritma:
Anki benzeri SM-2 (Spaced Repetition) algoritması.
Zorluk seviyesine göre soru sıklığını dinamik ayarlama.

Dark mod olsun
modern tasarım
arkaplan renkleri dark metin renkleri light olsun
iphone hesap makinesi tuş takımı olsun
kullanıcı cevabın basamak sayısı kadar tuşa bastığında enter tuşuna basıllmış sayılacak ve  uygulama kullancıya yeni bir soru soracak
ve uygulama bu şekilde belirlenen süre sonuna kadar  veya kullanıcı sonlandırana kadar soru soracak. tuşlar 70px*70px olacak.
kullanıcı 30 saniye 60 saniye ve süresiz seçeneklerden birini seçecek.
kullanıcının doğru yanlış cevaplarının sayısı ekranda görüntülenecek.
kullanıcının yanlış cevapladığı sorular daha sık tekrar edilecek.
kullanıcının doğru cevapladığı soruların tekrar aralığı artacak.
dogrular yeşil yanlışlar kırmızı renkte görüntülenecek.
git kullanalım.


kullanıcı eğer yanlış cevaplarsa o soru tekrar tekrar sorulacak
kullanıcı eğer doğru cevaplarsa o soru tekrar tekrar sorulmayacak


