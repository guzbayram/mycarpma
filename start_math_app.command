#!/bin/zsh

# Uygulama dizinine git
cd /Users/bayramguz/Documents/benimUygulamalarım/matUygulamalari/myCarpma

# Virtual environment'ı aktifleştir
source venv/bin/activate

# Django sunucusunu başlat (arka planda) ve PID'sini kaydet
python manage.py runserver & 
DJANGO_PID=$!

# 2 saniye bekle (sunucunun başlaması için)
sleep 2

# Safari'yi aç
open -a Safari http://127.0.0.1:8000

# Terminal penceresini gizle
osascript -e 'tell application "Terminal" to set visible of window 1 to false'

# Safari kapanana kadar bekle ve sonra Django sunucusunu kapat
while true; do
    if ! pgrep -x "Safari" > /dev/null; then
        kill $DJANGO_PID
        exit 0
    fi
    sleep 1
done 