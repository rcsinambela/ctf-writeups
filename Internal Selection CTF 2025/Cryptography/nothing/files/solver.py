# solve.py
import re

# Paste di sini isi variable flag persis seperti di soal.
# Gunakan r'...' (raw string) jika isi mengandung backslash supaya tidak diinterpretasi sebagai escape.
flag = r"                                                                       \t                                                                  \t                                                                                  \t                                                                                                                          \t                                                                                                                  \t                                                                                                 \t                                                                                                              \t                                                                                                                       \t                                                                                              \t                                                                                                        \t                                                                                                                  \t                                                                                              \t                                                                                                                     \t                                                                                                    \t                                                                                                                 \t                                                                                                                        \t                                                                                              \t                                                                                                  \t                                                                                                              \t                                                                                                              \t                                                                                                           \t                                                                                              \t                                                                                              \t                                                                                                \t                                                                                                                        \t                                                                                                \t                                                                                                                        \t                                                                                                \t                                                                                                                            \t"

# Split pada literal "\t" atau actual tab \t
parts = re.split(r'\\t|\t', flag)

# Hapus segmen kosong
parts = [p for p in parts if p != ""]

# Untuk tiap segmen: jumlah spasi + 1 => ASCII code
chars = [chr(len(p) + 1) for p in parts]

# Gabungkan
decoded = ''.join(chars)
print(decoded)
