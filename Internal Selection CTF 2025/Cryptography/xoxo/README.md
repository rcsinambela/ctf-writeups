# xoxo

Author:Vaa

Category: Cryptography

Flag: `HCS{r3p34t1ng_x0r_1s_t00_w34k_xoxo}`

## Description

They tried to keep a secret in the relationship, but their habits gave everything away.

## TLDR

Diberi ciphertext (hex) hasil XOR antara flag (FLAG = "HCS{placeholder}") dan sebuah key 4-byte yang diulang (repeating key).

## Analisis

Key hanya 4 byte tapi diulang untuk seluruh pesan → ini repeating-key XOR (sering juga disebut Vigenère/XOR dengan key pendek).

Jika format pesan diketahui sebagian (crib = known plaintext), saya bisa mengekstrak key dengan XOR sederhana:
key = ciphertext_prefix XOR crib.

CTF menggunakan format HCS{...} → ini adalah crib yang sangat berguna.

Diberikan juga Ciphertext: d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e

## Solution

1. Ambil 4 byte pertama ciphertext (hex bytes) dan XOR dengan 'H' 'C' 'S' '{':

- ciphertext bytes (4 pertama): d6 1a 70 19

- crib bytes: H C S { → 0x48 0x43 0x53 0x7b

2. Perhitungan XOR:

- 0xd6 XOR 0x48 = 0x9e

- 0x1a XOR 0x43 = 0x59

- 0x70 XOR 0x53 = 0x23

- 0x19 XOR 0x7b = 0x62

- -> key (4 bytes) = 0x9e 0x59 0x23 0x62 → hex: 9e592362

- (Ini juga bisa dituliskan sebagai bytes: b'\x9eY#b'.)

3. Gunakan key yang diulang (cycle) untuk XOR balik seluruh ciphertext -> akan menghasilkan plaintext/flag.

4. Jalankan solver.py

5. Didapatkan `HCS{r3p34t1ng_x0r_1s_t00_w34k_xoxo}`
