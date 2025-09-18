from itertools import cycle

ct_hex = "d61a7019ec6a5351aa2d120cf9065b52ec061211c12d1352c12e1056f5065b0de6365e"
ct = bytes.fromhex(ct_hex)
# asumsi crib
crib = b"HCS{"
key = bytes(a ^ b for a,b in zip(ct[:4], crib))
pt = bytes([c ^ k for c,k in zip(ct, cycle(key))])
print(pt.decode())
