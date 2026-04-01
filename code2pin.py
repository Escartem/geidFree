import hashlib

# XIANSH
code = "ABCDE-FGHIJ-KLMNO-PQRST-UVWXY"
code = "COXED-IDIOT-APPLE-NUTSY-EHHHH"
code = "AAAX-AAAX-AAAX-AAAX-AAAX-AAAX-A"
code = "XXXXX-IIIII-AAAAA-NSSSS-HHHHH"

def transform(inp: str):
	assert len(inp) >= 24
	out = ""
	for i in range(6):
		chunk = inp[i*4:(i+1)*4]
		c0 = ord(chunk[0])
		idx = c0 % 3
		v7 = chunk[idx + 1]
		out += v7
	return out

code = "".join(code.split("-"))
encoded = f"z{transform(code)}rh".encode("utf-8")
print(encoded)
md5 = hashlib.md5(encoded).digest()

pin = bytearray(md5[0:8])[::-1].hex().upper()

print(pin)

# 61053FA7D2C3B2C8
# 61053FA7D2C3B2C8


# CA AD E3 16 F7 4F F5 7D

# 7d F5 4F F7 16 E3 AD CA
# 7df54ff716e3adca