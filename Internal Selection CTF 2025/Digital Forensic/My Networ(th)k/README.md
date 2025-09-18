# My Networ(th)k

Author:Rev

Category: Digital Forensic

Flag: `HCS{kalian_langsung_filter_flagnya_atau_perhatiin_apa_attackernya_lakukan_hehe}`

## Description

Abis capture network website gweh, tentunya gada yang aneh lah ya?

## Solution

1. File -> Export objects -> http -> save all

2. Buka setiap file yang ada

3. Cari string yang unik dan didapat `e2thbGlhbl9sYW5nc3VuZ19maWx0ZXJfZmxhZ255YV9hdGF1X3BlcmhhdGlpbl9hcGFfYXR0YWNrZXJueWFfbGFrdWthbl9oZWhlfQ%3D%3D`

4. Gunakan URL decode dan hasilnya akan menjadi `e2thbGlhbl9sYW5nc3VuZ19maWx0ZXJfZmxhZ255YV9hdGF1X3BlcmhhdGlpbl9hcGFfYXR0YWNrZXJueWFfbGFrdWthbl9oZWhlfQ==`

5. Jalankan perintah `echo e2thbGlhbl9sYW5nc3VuZ19maWx0ZXJfZmxhZ255YV9hdGF1X3BlcmhhdGlpbl9hcGFfYXR0YWNrZXJueWFfbGFrdWthbl9oZWhlfQ==" | base64 -d`

6. flag yang ditemukan `{kalian_langsung_filter_flagnya_atau_perhatiin_apa_attackernya_lakukan_hehe}`