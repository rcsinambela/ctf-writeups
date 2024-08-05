# dont-use-client-side

Author: Alex Fulton/Danny

Category: Web Exploitation

Flag: `picoCTF{no_clients_plz_7723ce}`

## Description

Can you break into this super secure portal? https://jupiter.challenges.picoctf.org/problem/29835/ (link) or http://jupiter.challenges.picoctf.org:29835

## Difficulty

Easy

## Solution

1. Visit the website and then gather information

2. I checked the source code and it has the flag

```
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '723c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_7') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'e}') {
                  alert("Password Verified")
                  }
                }
              }

            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
  }
```

3. Check 1:
   if (checkpass.substring(0, split) == 'pico')

   The first 4 characters (substring from 0 to 4) must be pico.

4. Check 2:
   if (checkpass.substring(split*6, split*7) == '723c')

   Characters from position 24 to 28 (substring from 24 to 28) must be 723c.

5. Check 3:
   if (checkpass.substring(split, split\*2) == 'CTF{')

   Characters from position 4 to 8 (substring from 4 to 8) must be CTF{.

6. Check 4:
   if (checkpass.substring(split*4, split*5) == 'ts_p')

   Characters from position 16 to 20 (substring from 16 to 20) must be ts_p.

7. Check 5:
   if (checkpass.substring(split*3, split*4) == 'lien')

   Characters from position 12 to 16 (substring from 12 to 16) must be lien.

8. Check 6:
   if (checkpass.substring(split*5, split*6) == 'lz_7')

   Characters from position 20 to 24 (substring from 20 to 24) must be lz_7.

9. Check 7:
   if (checkpass.substring(split*2, split*3) == 'no_c')

   Characters from position 8 to 12 (substring from 8 to 12) must be no_c.

10. Check 8:
    if (checkpass.substring(split*7, split*8) == 'e}')

    Characters from position 28 to 32 (substring from 28 to 32) must be e}.

Combining these substrings together in the correct order gives us the full flag:

First part: pico

Second part: CTF{

Third part: no_c

Fourth part: lien

Fifth part: ts_p

Sixth part: lz_7

Seventh part: 723c

Eighth part: e}

Putting it all together, the flag is:
picoCTF{no_clients_plz_7723ce}
