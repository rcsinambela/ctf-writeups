# Roboto Sans

Author:

Category: Web Exploitation

Flag: `picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}`

## Description

The flag is somewhere on this web application not necessarily on the website. Find it.

## Difficulty

Medium

## Solution

1. Visit the website

2. Go to robots.txt -> `http://saturn.picoctf.net:54402/robots.txt`

3. You'll see `anMvbXlmaWxlLnR4dA==`

4. Decode it and the output will be `js/myfile.txt`

5. Visit it `http://saturn.picoctf.net:54402/js/myfile.txt`

6. You'll meet the flag
