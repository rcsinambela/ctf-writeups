# Irish-Name-Repo 2

Author: Xingyang Pan

Category: Web Exploitation

Flag: `picoCTF{m0R3_SQL_plz_c34df170}`

## Description

There is a website running at https://jupiter.challenges.picoctf.org/problem/53751/ (link). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751

## Difficulty

Medium

## Solution

1. Visit the website

2. Open menu and go to `Admin Login`

3. Just use this payload `'=0--`

![POC 1](image.png)

4. I try many payloads but it doesn't work
