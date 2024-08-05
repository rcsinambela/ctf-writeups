# Power Cookie

Author: LT 'syreal' Jones

Category: Web Exploitation

Flag: `picoCTF{gr4d3_A_c00k13_0d351e23}`

## Description

Can you get the flag?
Go to this website and see what you can discover.

## Difficulty

Medium

## Solution

1. Visit the website

2. Check all the source code

3. You'll see `<script src="guest.js"></script>` just click it

4. You'll see JavaScript function

```
function continueAsGuest()
{
  window.location.href = '/check.php';
  document.cookie = "isAdmin=0";
}
```

5. I think there will be a cookie cause I see `document.cookie = "isAdmin=0";`

6. So back to the website and tap button `Continue as guest`

![POC 1](image.png)

7. Change the value from 0 to 1 and dont forget to save it

![POC 2](image-1.png)

8. Refresh the website

9. You'll see the flag
