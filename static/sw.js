// Cache ismi ve versiyonu
const CACHE_NAME = 'math-app-v1';

// Önbelleğe alınacak dosyalar
const urlsToCache = [
    '/',
    '/static/manifest.json',
    '/static/icons/icon-192x192.png',
    '/static/icons/icon-512x512.png',
    '/practice/',
];

// Service Worker kurulumu
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Önbellek açıldı / Cache opened');
                return cache.addAll(urlsToCache);
            })
    );
});

// Fetch olaylarını yakala
self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Cache'de varsa cache'den döndür
                if (response) {
                    return response;
                }
                // Cache'de yoksa network'den al
                return fetch(event.request);
            })
    );
});

// Cache güncelleme
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
}); 