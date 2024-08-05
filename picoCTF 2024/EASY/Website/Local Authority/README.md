# Local Authority

Author: LT 'syreal' Jones

Category: Web Exploitation

Flag: `picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}`

## Description

Can you get the flag?
Additional details will be available after launching your challenge instance.

## Difficulty

Easy

## Solution

1. Visit the website and then inspect it

2. Go to network

3. For the first I thought I must use it `(Only letters and numbers allowed for username and password.)`

4. So I typed admin123 (actually you can use rnadom password) for username and password

5. Go to Network tab

6. You'l see secure.js like below

```
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

7. So, just type it into the form

8. You'll get the flag
