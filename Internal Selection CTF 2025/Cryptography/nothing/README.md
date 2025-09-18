# nothing

Author:Hanz

Category: Cryptography

Flag: `HCS{sbox_is_very_cool__ayaya}`

## Description

A subtitution cipher? naah, this is Nothing Cipher (TM)

## TLDR

Diberikan sebuah SBox mapping dan sebuah variabel flag yang tampak seperti gabungan banyak blok: setiap blok berakhir dengan \t.

Setiap blok terdiri dari sejumlah spasi diikuti \t (kadang representasinya muncul sebagai dua karakter \ dan t).

Hipotesis: setiap blok merepresentasikan sebuah angka (index) berdasarkan jumlah spasi, lalu angka itu dikonversi menjadi karakter ASCII → menghasilkan pesan / flag.

## Analisis

Perhatikan SBox (contoh): SBox[1] = '\t', SBox[2] = ' \t', SBox[3] = ' \t', ...
Artinya: untuk integer i, representation = ' '*(i-1) + '\t'.

Jadi jika saya menemukan satu blok dengan n spasi lalu \t, maka angka yang tersandi = n + 1.

Konversi tiap angka tersebut ke karakter ASCII (chr(n+1)) menghasilkan karakter pesan.

## Solution

1. Ambil string flag dari soal.

2. Pecah string menjadi blok-blok dengan mem-split pada \t (masalah: bisa berupa actual tab \t atau literal \\t di teks).

3. Hapus blok kosong yang mungkin muncul karena trailing/leading split.

4. Untuk setiap blok, hitung banyaknya spasi → n.

5. Ambil n + 1 → ini adalah nilai ASCII.

6. Konversi tiap nilai menjadi karakter (chr(n+1)), gabungkan semua → dapat flag.

7. Jalankan solver.py

8. Didapatkan `HCS{sbox_is_very_cool__ayaya}`
