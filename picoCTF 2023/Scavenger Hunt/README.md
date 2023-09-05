![POC 1](/snake/images/poc1.png)# Cookies

Author: zaratec/danny

Category: Web Exploitation

Flag: `HCS{ez_game_right?_74ab}`

## Description
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ (link) or http://jupiter.challenges.picoctf.org:41511

## Difficulty
Easy

## Solution

Pertama saya buka link tersebut

Kedua, klik kanan pada mouse atau touch pad dan pilih view page source

Ketiga, liat semua source codenya dan fokus ke bagian comment html, di sana ada potongan flag `<!-- Here's the first part of the flag: picoCTF{t -->`

![POC 1](/snake/images/poc1.png)

Keempat, kunjungi css dan script js yang ada di header html

Kelima, saya menemukan potongan flag yang kedua `/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */` di file css

![POC 2](/snake/images/poc1.png)

Keenam, saat mengunjungi file js terdapat pertanyaan `/* How can I keep Google from indexing my website? */`

![POC 3](/snake/images/poc1.png)

Simplenya gini, bagaimana cara si developer menyembunyikan suatu file/directory agar tidak diindex oleh Google

Jawabannya ada di robots.txt, untuk robots.txt bisa kalian pelajari sendiri

Saat mengakses robots.txt, saya menemukan potongan flag `# Part 3: t_0f_pl4c` dan pertanyaan lagi `# I think this is an apache server... can you Access the next flag?`

Untuk mengelola web server Apache ada file `.htaccess`

Saat mengakses `.htaccess`, saya menemukan potongan flag `# Part 4: 3s_2_lO0k` dam pertanyaan lagi `# I love making websites on my Mac, I can Store a lot of information there.`

Saya mencari di browser dengan keyword `Store information web mac` dan saya menemukan sebuah judul halaman yang unik, yaitu `.DS_Store`

Setelah itu langsung aja akses `.DS_Store` dan saya menemukan potongan flag yang terakhir `Congrats! You completed the scavenger hunt. Part 5: _d375c750}`

![POC 3](/snake/images/poc1.png)