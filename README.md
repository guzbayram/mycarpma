# MyCarpma

Matematik işlemleri alıştırma uygulaması. Bu uygulama ile çarpma, bölme, toplama ve çıkarma işlemlerini pratik yapabilirsiniz.

## Özellikler

- Çarpma işlemi alıştırmaları
- Bölme işlemi alıştırmaları
- Toplama işlemi alıştırmaları
- Çıkarma işlemi alıştırmaları
- Süre tutma özelliği
- Skor takibi
- PWA desteği (Progressive Web App)

## Kurulum

1. Python 3.10 veya üzeri sürümü yükleyin
2. Sanal ortam oluşturun:

```bash
python -m venv venv
source venv/bin/activate  # MacOS için
```

3. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

4. Veritabanını oluşturun:

```bash
python manage.py migrate
```

5. Sunucuyu başlatın:

```bash
python manage.py runserver
```

## Teknolojiler

- Django 4.2.19
- Python 3.10
- Bootstrap 5
- JavaScript
- PWA (Progressive Web App)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
