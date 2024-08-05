# Forbidden Paths

Author: LT 'syreal' Jones

Category: Web Exploitation

Flag: `picoCTF{7h3_p47h_70_5ucc355_6db46514}`

## Description

Can you get the flag?
We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?
Here's the website.

## Difficulty

Medium

## Solution

1. Visit the website

2. From the description, it tells where the website files live `/usr/share/nginx/html/`

3. It likes path traversal, so our working directory in html, so you must go to / (root) cause the flag in /flag.txt (root)

4. ../../../../flag.txt

5. You'll see the flag
