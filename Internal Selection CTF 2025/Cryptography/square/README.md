# square

Author:Hanz

Category: Cryptography

Flag: `HCS{this_math_thing_is_confusing__ayaya}`

## Description

RSA is very easy that I can implement my own!

## TLDR

Soal menggunakan q = p sehingga modulus RSA N = p * q = p² — kesalahan fatal. Karena N adalah kuadrat sempurna, saya bisa ambil akar kuadrat bulatnya untuk menemukan p, lalu menghitung φ(N) = φ(p²) = p*(p-1). Setelah itu saya hitung invers d ≡ e⁻¹ (mod φ(N)) dan dekripsi ciphertext m ≡ ct^d (mod N) untuk mendapatkan pesan (flag).

## Teorinya seperti ini

Normalnya RSA: N = p * q dengan p != q.

Jika q = p, maka N = p². Jadi p = sqrt(N).

Euler totient untuk p² adalah φ(p²) = p² - p = p*(p-1).

Dengan φ(N) diketahui, kunci privat d ditemukan sebagai invers e modulo φ(N).

Dekripsi: m = ct^d mod N.

## Solution

1. Jalankan solver.py

2. Didapatkan `HCS{this_math_thing_is_confusing__ayaya}`
