# Reverse Day 1

Author:erzyyyy

Category: Reverse Engineering

Flag: `HCS{reverse_is_eazyyyy}`

## Description

## Solution

Coba cari informasi dari file chall

```
➜  ctf-writeups git:(main) ✗ file Internal\ Selection\ CTF\ 2025/Reverse\ Engineering/Reverse\ Day\ 1/files/chall
Internal Selection CTF 2025/Reverse Engineering/Reverse Day 1/files/chall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=fda9172d945048b313253f8526b84d3e75ddbb51, for GNU/Linux 3.2.0, not stripped
➜  ctf-writeups git:(main) ✗ ldd Internal\ Selection\ CTF\ 2025/Reverse\ Engineering/Reverse\ Day\ 1/files/chall
        linux-vdso.so.1 (0x00007bf5cf740000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007bf5cf400000)
        /lib64/ld-linux-x86-64.so.2 (0x00007bf5cf742000)
➜  ctf-writeups git:(main) ✗ strings Internal\ Selection\ CTF\ 2025/Reverse\ Engineering/Reverse\ Day\ 1/files/chall | egrep 'HCS|Usage|Incorrect'
HCS{faaakeeeflaaaaaaag}
Usage: %s <flag>
Incorrect length!
```

1. Jalankan `chmod +x chall`
2. Run `./chall` akan muncul pesan di terminal `Usage: ./chall <flag>`
3. Saat menjalankan `./chall test` muncul pesan `Incorrect length!`
4. lalu saat menjalankan perintah

    ```
    python3 - <<'PY'
    from subprocess import Popen, PIPE
    for n in range(1,60):
        p = Popen(['./chall','A'*n], stdout=PIPE, stderr=PIPE, text=True)
        out,err = p.communicate(timeout=1)
        if 'Incorrect length' not in out:
            print(n, out.strip())
    PY
    ```

    muncul pesan 23 Wrong!

    Kesimpulan: panjang flag yang diharapkan = 23 bytes (termasuk HCS{...}).

5. Disassembly fungsi check. Karena binary tidak stripped, kita bisa disassemble fungsi check: `objdump -d -M intel --no-show-raw-insn --disassemble=check chall > check_disasm.txt`

6. Interpretasi singkat:

- Program memuat 23 byte literal yang tersebar di beberapa instruksi movabs, mov (8+8+4+2+1 = 23 bytes). Itu adalah ciphertext.

- Key XOR disimpan di BYTE PTR [rbp-0x69] dengan nilai 0x5e (instruksi mov BYTE PTR [rbp-0x69],0x5e).

- Loop membaca tiap byte ciphertext, melakukan xor dengan key 0x5e, menyimpan hasil ke buffer, lalu membandingkan tiap byte input pengguna dengan buffer hasil decode. Jika semua match, program akan lanjut (print success); else puts("Wrong!") dan exit.

7. Rekonstruksi literal bytes (endianness penting)

    Dari movabs/mov/mov immediate di assembly kita dapat mengambil byte-by-byte literal (ingat movabs rax,0x1122334455 menyimpan immediate dalam little-endian ketika dilihat di memori).

    Kompilasi fragmen yang kita lihat:

    movabs rax,0x3b283b2c250d1d16 -> 8 bytes (LE): 16 1d 0d 25 2c 3b 28 3b

    movabs rdx,0x3b012d37013b2d2c -> 8 bytes (LE): 2c 2d 3b 01 37 2d 01 3b

    mov DWORD PTR [rbp-0x40],0x2727243f -> 4 bytes (LE): 3f 24 27 27

    mov WORD PTR [rbp-0x3c],0x2727 -> 2 bytes: 27 27

    mov BYTE PTR [rbp-0x3a],0x23 -> 1 byte: 23

    Gabungkan (urutan sesuai disassembly) → 23 bytes ciphertext:
    `16 1d 0d 25 2c 3b 28 3b 2c 2d 3b 01 37 2d 01 3b 3f 24 27 27 27 27 23`

8. Decode: XOR tiap byte dengan kunci 0x5e

   Lakukan XOR per byte dengan 0x5e (karena loop menggunakan xor al, BYTE PTR [rbp-0x69] dan kita lihat mov BYTE PTR [rbp-0x69],0x5e):

   Hasil XOR (hex) → ASCII:

   ```
   48 43 53 7b 72 65 76 65 72 73 65 5f 69 73 5f 65 61 7a 79 79 79 79 7d
   -> "HCS{reverse_is_eazyyyy}"
   ```