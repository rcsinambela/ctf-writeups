# check it out

Author:TinyTidy

Category: Reverse Engineering

Flag: `HCS{Ju4G0_Bw4nG}`

## Description

Don't forget to check it.

## Solution

1. Buka file Main.java dengan editor (vim/code/etc).

2. Cari bagian if (characters[0] == 'H') dan seterusnya — program mengecek 16 karakter berurutan.

3. Baca karakter yang dibandingkan untuk setiap indeks, urutkan dari 0 sampai 15.

    ```
    Hasil pembacaan (dari kode):

    characters[0] == 'H'

    characters[1] == 'C'

    characters[2] == 'S'

    characters[3] == '{'

    characters[4] == 'J'

    characters[5] == 'u'

    characters[6] == '4'

    characters[7] == 'G'

    characters[8] == '0'

    characters[9] == '_'

    characters[10] == 'B'

    characters[11] == 'w'

    characters[12] == '4'

    characters[13] == 'n'

    characters[14] == 'G'

    characters[15] == '}'
    ```

4. final flag: `HCS{Ju4G0_Bw4nG}`