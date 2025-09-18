# Atadatem

Author:Bim

Category: Reverse Engineering

Flag: `HCS{metadata_can_be_useful_somewhere_somehow_sometime}`

## Description

look there are data that seperated!! you should combine them!

## Solution

1. Jalankan perintah `exiftool hcs.png `

2. Ada petunjuk di bagian title

   ```
   Comment                         : UUF6NjZDdXEvb
   Description                     : 2FwLy86c3B0dGg=
   Title                           : Comments - Keywords - Description
   Keywords                        : W9jLm5pYmV0c
   ```

3. Kalau diurutkan menjadi `UUF6NjZDdXEvbW9jLm5pYmV0c2FwLy86c3B0dGg=`

4. Jalankan perintah `echo "UUF6NjZDdXEvbW9jLm5pYmV0c2FwLy86c3B0dGg=" | base64 -d` dan dipatkan `QAz66Cuq/moc.nibetsap//:sptth`

5. Gunakan tools reverse string dan didapat `https://pastebin.com/quC66zAQ`

6. Jalankan perintah `echo "e21ldGFkYXRhX2Nhbl9iZV91c2VmdWxfc29tZXdoZXJlX3NvbWVob3dfc29tZXRpbWV9" | base64 -d`

7. hasilnya: `{metadata_can_be_useful_somewhere_somehow_sometime}`