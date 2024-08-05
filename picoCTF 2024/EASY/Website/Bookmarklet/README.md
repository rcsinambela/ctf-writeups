# Bookmarklet

Author: Jeffery John

Category: Web Exploitation

Flag: `picoCTF{p@g3_turn3r_1d1ba7e0}`

## Description

Why search for the flag when I can make a bookmarklet to print it for me?
Browse here, and find the flag!

## Difficulty

Easy

## Solution

1. Kunjungi websitenya dan cari informasi apa aja yang bisa didapatkan

2. Saya lebih suka lihat source codenya langsung secara keseluruhan

![POC 1](image.png)

3. Karena saya belum pernah menangani kasus terkait bookmarklet di JavaScript jadi saya pelajari dulu

4. Setelah paham saya copy source codenya terlebih dahulu

![POC 2](image-1.png)

5. Paste ke browser dan tambahkan `javascript: ` karena ikut terhapus

6. Dan flagnya muncul

![POC 3](image-2.png)
