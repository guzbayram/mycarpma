#!/usr/bin/osascript

on run
    -- Önce Safari'yi kapat ve bekle
    tell application "Safari" to quit
    delay 1
    
    -- Django sunucusunu başlat (0.0.0.0 ile tüm IP'lerden erişime izin ver)
    do shell script "cd /Users/bayramguz/Documents/benimUygulamalarım/matUygulamalari/myCarpma && source venv/bin/activate && python manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1 &"
    
    -- 2 saniye bekle (sunucunun başlaması için)
    delay 2
    
    -- Safari'yi başlat ve URL'yi yükle (3 deneme hakkı)
    repeat with i from 1 to 3
        try
            tell application "Safari"
                activate
                delay 1
                
                -- Yeni pencere aç
                close every window
                make new document
                set URL of document 1 to "http://192.168.1.101:8000"
                set bounds of window 1 to {50, 50, 1200, 800}
                
                -- URL yüklenene kadar bekle (maksimum 5 saniye)
                repeat with waitCount from 1 to 5
                    if URL of current tab of window 1 contains "192.168.1.101:8000" then
                        exit repeat
                    end if
                    delay 1
                end repeat
                
                -- URL kontrolü başarılıysa döngüden çık
                if URL of current tab of window 1 contains "192.168.1.101:8000" then
                    exit repeat
                end if
            end tell
        on error
            -- Hata durumunda 1 saniye bekle ve tekrar dene
            delay 1
        end try
    end repeat
    
    -- Ana döngü: Safari kapanana veya URL değişene kadar bekle
    repeat
        delay 1
        try
            tell application "Safari"
                if not (exists window 1) then
                    exit repeat
                end if
                
                set currentURL to URL of current tab of window 1
                if currentURL does not contain "192.168.1.101:8000" then
                    exit repeat
                end if
            end tell
        on error
            exit repeat
        end try
    end repeat
    
    -- Django sunucusunu kapat
    do shell script "pkill -f 'python manage.py runserver'"
    
    -- Script'i sonlandır
    quit
end run

on quit
    -- Temiz kapatma için
    try
        do shell script "pkill -f 'python manage.py runserver'"
    end try
    continue quit
end quit 