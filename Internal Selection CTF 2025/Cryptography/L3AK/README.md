# Atadatem

Author:etern1ty

Category: Cryptography

Flag: `HCS{leak_l3ak_l34k_i_hate_leaks_65746572}`

## Description

what is what?

## TLDR

Diberikan: n, ct (ciphertext), dan what = d % (p-1).

Karena what ≡ d (mod (p-1)) dan e·d ≡ 1 (mod (p-1)), maka e*what ≡ 1 (mod (p-1)).

Untuk bilangan a yang bukan kelipatan p, berlaku a^(e*what) ≡ a (mod p) sehingga p | (a^(e*what) - a).

Maka g = gcd(a^(e*what) - a, n) akan memberikan faktor non-trivial (yaitu p) dengan probabilitas tinggi.

Setelah menemukan p, hitung q = n // p, phi = (p-1)(q-1), hitung d = e^{-1} mod phi, lalu dekripsi m = ct^d mod n.

## Solution

1. Data yang diberikan

   ```
   n = 132424945097525850654214822436841749617596013766516589461846053019923921509419349878188173267137393388564369574894943951802964034938666342594121858359017467945336230806773103437033058400722533249173019431218833060574032187854004778243330232248639993250668984287478087484530899867973181768171106834615858816947
   ct = 8690256152525015206584791844752543379719744787620368046544606811870676380837374553817755653019413372016870108768104936568432345008226950086769230094097164464486596908050930851678115904352532562944170575365724833300330295692157262447360439786705110831106538310141401194897207768598781335529794463310318530218
   what = 4701066001566933468539295457165541117336002410834834617743586840140912396231299819496271034686173752299173098904260222360140687146281504574213995930648721
   e = 65537
   ```

   Nilai what adalah bocoran (leak) dari d modulo (p-1) — informasinya cukup untuk membongkar salah satu faktor p.

2. Penjelasan

   '''
   Karena what ≡ d (mod (p-1)), maka ada integer t sehingga d = what + t*(p-1).

   Karena e*d ≡ 1 (mod phi) dan phi = (p-1)(q-1) maka khusus modulo p-1 berlaku e*d ≡ 1 (mod (p-1)).

   Maka e*what ≡ e*d ≡ 1 (mod (p-1)).

   Dengan menulis e*what = 1 + k*(p-1) untuk suatu integer k, untuk setiap a yang tidak kelipatan p:

   a^(e*what) = a^(1 + k*(p-1)) = a * (a^(p-1))^k ≡ a * 1^k ≡ a (mod p).

   Jadi p | (a^(e*what) - a). Oleh karena n = p*q, kita ambil g = gcd(a^(e*what) - a, n); jika g bukan 1 atau n, maka g adalah salah satu faktor prima (p atau q).

   Dengan mengambil beberapa nilai a kecil (mis. 2, 3, 5, ...), probabilitas memperoleh faktor non-trivial sangat tinggi.
   '''

3. Step by step to exploit

   ```
   Simpan nilai n, ct, what, dan e ke dalam script.

   Jalankan loop untuk beberapa basis a kecil (2,3,5,7,...) dan hitung g = gcd(pow(a, e*what, n) - a, n).

   Jika 1 < g < n, maka p = g. Hentikan loop.

   Jika tidak ketemu, lakukan percobaan dengan basis random sampai ketemu.

   Hitung q = n // p dan verifikasi p*q == n.

   Hitung phi = (p-1)*(q-1) dan d = inverse(e, phi).

   Dekripsi: m = pow(ct, d, n) lalu konversi: long_to_bytes(m).decode().
   ```

4. Jalankan script solver.py

5. Didapatkan `HCS{leak_l3ak_l34k_i_hate_leaks_65746572}`
