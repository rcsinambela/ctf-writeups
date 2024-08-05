# where are the robots

Author: zaratec/Danny

Category: Web Exploitation

Flag: `picoCTF{ca1cu1at1ng_Mach1n3s_8028f}`

## Description

Can you find the robots? https://jupiter.challenges.picoctf.org/problem/60915/ (link) or http://jupiter.challenges.picoctf.org:60915

## Difficulty

Easy

## Solution

1. Visit the website

2. There's a question `Where are the robots?` the answer is robots.txt

3. Just add robots.txt

![POC 1](image.png)

4. change `robots.txt` to `/8028f.html` from the url

5. You'll see the flag

![POC 2](image-1.png)
