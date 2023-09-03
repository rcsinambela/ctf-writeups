# Snake

Author: kosong

Category: Reverse Engineering

Flag: `HCS{ez_game_right?_74ab}`

## Description
Capai skor tertentu untuk mendapatkan flag.

## Difficulty
Easy

## Solution

Pertama saya mencoba menjalankan `index.html` dan melihat seperti sebuah game 

Lalu saya membuka ketiga file `app.css app.js dan index.html` untuk melihat source codenya

Selanjutnya saat saya melihat code yang ada di `app.js` itu sangat berantakan dan susah dibaca jadi saya merapihkannya menggunakan https://beautifier.io/

Lalu saat saya source code seperti di bawah ini:

![POC 1](/snake/images/poc1.png)

Saya menemukan sesuatu yang unik yaitu, playerScore = 0x0

Setelah itu saya cari `score` seperti gamber di bawah ini

![POC 2](/snake/images/poc2.png)

Lalu ubah playerScore = 0x0 dan save

Setelah itu tinggal buka file `index.html` atau reload jika sebelumnya sudah dirun

Tap start button dan biarkan kalah

![POC 2](/snake/images/poc3.png)

