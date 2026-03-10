🛰️ Akıllı Tarım Destek Sistemi - Proje Akış Planı
Proje, verinin topraktan alınıp yapay zeka ile işlenerek çiftçiye ulaştırılmasına kadar 4 ana aşamadan oluşmaktadır:

1. Aşama: Gereksinim Analizi ve Veri Hazırlığı (Hafta 1-2)
Gereksinim Belgeleme: İşlevsel ve teknik gereksinimlerin yazılması (Şu an yaptığın aşama).

Veri Kaynaklarının Belirlenmesi: * Hava durumu için OpenWeatherMap API vb. kullanımı.

Toprak analizi verileri için açık kaynaklı veri setleri (Kaggle vb.) veya sensör simülasyonu.

Veri Ön İşleme: Eksik verilerin tamamlanması, verilerin normalizasyonu ve temizlenmesi.

2. Aşama: Yapay Zeka ve Model Geliştirme (Hafta 3-5)
Model Seçimi: Tahminleme için TensorFlow/Keras kullanılarak Regresyon veya Sınıflandırma modellerinin kurulması.

Eğitim: Veri setinin %80 eğitim, %20 test olarak ayrılıp modelin eğitilmesi.

Öneri Motoru: Toprak analizi sonuçlarına göre (Azot, Fosfor, Potasyum seviyeleri) hangi gübrenin ne kadar atılması gerektiğini hesaplayan kural tabanlı sistemin entegre edilmesi.

3. Aşama: Arka Uç (Backend) ve Bulut Entegrasyonu (Hafta 6-7)
API Geliştirme: Yapay zeka modelini bir web servisi (Flask veya FastAPI) haline getirmek.

Bulut Dağıtımı: Sistemin Bulut Bilişim (Azure, Google Cloud veya AWS) üzerinde yayına alınması.

Veri Tabanı: Kullanıcı bilgilerinin ve geçmiş tarım verilerinin kaydedilmesi.

4. Aşama: Arayüz Geliştirme ve Test (Hafta 8-10)
Kullanıcı Paneli: Çiftçilerin grafiklerle toprak durumunu görebileceği Web veya Mobil arayüzün tasarımı.

Entegrasyon: Arayüzün backend ile haberleşmesinin sağlanması.

Saha Testleri: Tahminlerin tutarlılığının kontrol edilmesi ve hata düzeltmeleri.

Teslim Edilecek Temel Modüller
✅ Veri İşleme Modülü: Ham veriyi modele hazır hale getirir.

✅ Tahmin Algoritması: En uygun ekim zamanını belirler.

✅ Öneri Sistemi: Gübreleme ve sulama tavsiyeleri verir.

✅ Kullanıcı Arayüzü: Tüm bu verileri görselleştirir.
