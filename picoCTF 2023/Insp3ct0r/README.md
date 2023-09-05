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

Ketiga, liat semua source codenya dan fokus ke bagian comment html, di sana ada potongan flag `<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->`

![POC 1](/snake/images/poc1.png)

Keempat, kunjungi css dan script js yang ada di header html

Kelima, saya menemukan potongan flag yang kedua `/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */` di css

![POC 2](/snake/images/poc1.png)

Keenam, saya menemukan potongan flag terakhir `/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */` di js

![POC 3](/snake/images/poc1.png)