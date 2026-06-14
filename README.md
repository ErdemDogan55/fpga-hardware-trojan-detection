# fpga-hardware-trojan-detection
YZ Destekli FPGA Tabanlı Donanım Truva Atı Tespit Sistemi

# FPGA Tabanlı Donanım Truva Atı Tespit Sistemi

> YZ Destekli Donanım Güvenliği Test ve Eğitim Prototipi

## Proje Hakkında
Bu proje, FPGA üzerinde emüle edilen donanım truva atlarını 
yan kanal analizi (güç, akım, sıcaklık) ve makine öğrenmesi 
ile tespit eden açık kaynak bir araştırma prototipidir.

## Donanım
- 2x Digilent Cmod A7-35T FPGA
- Raspberry Pi Pico
- INA226 Güç/Akım Sensörü
- Breakout (Shunt) Kartı

## Klasör Yapısı
- `/fpga` → Verilog tasarımları (golden + trojan)
- `/pico` → INA226 ölçüm yazılımı
- `/ai`   → Makine öğrenmesi modelleri (yakında)
- `/data` → Ölçüm veri setleri (yakında)
- `/docs` → Proje raporu

## Durum
🔄 Geliştirme aşamasında
