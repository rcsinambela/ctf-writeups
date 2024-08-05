# picobrowser

Author: Archit

Category: Web Exploitation

Flag: `picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}`

## Description

This website can be rendered only by picobrowser, go and catch the flag! https://jupiter.challenges.picoctf.org/problem/50522/ (link) or http://jupiter.challenges.picoctf.org:50522

## Difficulty

Medium

## Solution

1. Use your burpsuite

2. turn on your intercept and tap flag button

3. Change something `User-Agent: <something>` to picobrowser

![POC 1](image.png)

4. You'll get the flag
