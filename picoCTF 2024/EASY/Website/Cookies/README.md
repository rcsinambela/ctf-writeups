# Cookies

Author: madStacks

Category: Web Exploitation

Flag: `picoCTF{3v3ry1_l0v3s_c00k135_96cdadfd}`

## Description

Who doesn't love cookies? Try to figure out the best one. http://mercury.picoctf.net:54219/

## Difficulty

Easy

## Solution

1. Visit the website

![POC 1](image.png)

2. Input `snickerdoodle`

![POC 2](image-1.png)

3. Check the cookies

4. Tha value is increased from -1 to 0

5. I tried to modify the value

![POC 3](image-2.png)

6. and then it worked after I refreshed

![POC 4](image-3.png)

7. So I made a script for automation

![POC 5](image-4.png)

8. Boom, I got the flag
