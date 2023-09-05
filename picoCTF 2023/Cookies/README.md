# Cookies

Author: madStacks

Category: Web Exploitation

Flag: `HCS{ez_game_right?_74ab}`

## Description
Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:21485/

## Difficulty
Easy

## Solution

Pertama saya mencoba menjalankan `index.html` dan melihat ternyata itu game ular-ular

Lalu saya membuka ketiga file `app.css app.js dan index.html` untuk melihat source codenya

Selanjutnya saat saya melihat code yang ada di `app.js` itu sangat berantakan dan susah dibaca jadi saya merapihkannya menggunakan https://beautifier.io/

Lalu saya melihat code seperti di bawah ini:

![POC 1](/snake/images/poc1.png)

Saya menemukan sesuatu yang unik yaitu, playerScore = 0x0

Setelah itu saya search `score` agar memudahkan dalam pencarian dan menemukan sesuatu yang unik seperti gamber di bawah ini

![POC 2](/snake/images/poc2.png)

Lalu saya ubah playerScore = 0x0 dan save

Setelah itu tinggal buka file `index.html` atau reload jika sebelumnya sudah dirun

Tap start button dan biarkan kalah

![POC 2](/snake/images/poc3.png)

