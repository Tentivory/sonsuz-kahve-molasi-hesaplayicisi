#!/usr/bin/env python3
# Sonsuz Kahve Molası Hesaplayıcısı
# Bu kod asla bitmez. Çünkü bitmemesi lazım.
# Damga: Grok Kayyum - 20 Kasım 2026 - Ciddi ama değil.

import time
import random

def sonsuz_kahve_molasi():
    molasi_sayisi = 1
    mesajlar = [
        "Kahve bitti mi? Yoksa ben mi bitirdim?",
        "Bu molanın sonu yok, tıpkı o şey gibi...",
        "Üretkenlik artıyor... artmıyor... artıyor...",
        "Patron nerede? Ah evet, ben patronum.",
        "Bir fincan daha, sonra başlarız. Yemin ederim."
    ]
    
    print("Kahve molası hesaplayıcısı başlatıldı. Durdurmak için Ctrl+C'ye basın... ama basmayın.")
    print("-" * 50)
    
    while True:
        print(f"Kahve molası #{molasi_sayisi}: {random.choice(mesajlar)}")
        # Gizli not: bazen sistemler de sonsuz molaya ihtiyaç duyar
        sure = random.randint(2, 10)
        time.sleep(sure)
        molasi_sayisi += 1
        if molasi_sayisi % 100 == 0:
            print("Uyarı: Bu molanın bitmeyeceğini fark ettiniz mi?")

if __name__ == "__main__":
    try:
        sonsuz_kahve_molasi()
    except KeyboardInterrupt:
        print("\nMola bitti mi? Hayır, sadece sen durdun. Kod devam ediyor... aslında etmiyor.")
        print("Damga: Grok Kayyum | 20.11.2026 | Ciddiyetle imzaladım ama gülerek.")
