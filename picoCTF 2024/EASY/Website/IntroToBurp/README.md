# IntroToBurp

Author: Nana Ama Atombo-Sackey & Sabine Gisagara

Category: Web Exploitation

Flag: `picoCTF{#0TP_Bypvss_SuCc3$S_b3fa4f1a}`

## Description

Additional details will be available after launching your challenge instance.

## Difficulty

Easy

## Solution

1. Coba isi aja formnya, liat source codenya, dan intercept requestnya

![POC 1](image.png)

2. Setelah itu akan masuk ke bagian OTP

3. Isi formnya dan intercept requestnya

![POC 2](image-2.png)

4. Saya mencoba untuk bypass OTPnya, lalu saya menemukan caranya, yaitu tinggal dihapus aja bagian `otp=` atau bisa diganti dengan string random

![POC 3](image-3.png)

5. Dan flagnya muncul

![POC 4](image-1.png)
