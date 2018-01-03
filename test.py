import x13bcd_hash

from binascii import unhexlify, hexlify

block_hash = 'fd21da3c2b0b6e5f438d365ef3f9a2e3a5018b9402fff79bec0a2e47657e802b'
block_header_hex = '600000006df1d486138ba00b9ceabc42c71c9d1925ea25896ee5555e78507642be52a4d761f93e1f507975d05a33de16bea7784f5cf492aa8e0eda6bf71029d78e3d939a5a2fa97e1d08379f000b3a0e'
block_header_bin = unhexlify(block_header_hex)
block_hash_bin = x13bcd_hash.getPoWHash(b''.join([block_header_bin[i * 4:i * 4 + 4][::-1] for i in range(0, 20)]))
block_hash_hex = hexlify(block_hash_bin[::-1]).decode("utf-8")
assert block_hash_hex == block_hash
