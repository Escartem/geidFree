import hashlib
import itertools
import string
from tqdm import tqdm

target = "7df54ff716e3adca"
chars = string.ascii_letters[26:]

print(chars)

for combo in tqdm(itertools.product(chars, repeat=6), total=26**6):
    s = ''.join(combo)
    test = "z" + s + "rh"
    h = hashlib.md5(test.encode()).hexdigest()
    
    if h.startswith(target):
        print(s)
        break

# XIANSH
# ABCDE-FGHIJ-KLMNO-PQRST-UVWXY
#    D  F     K     P R     W
#    X  I     A     N   S   H

# FLOXY-IDIOT-APPLE-NASTY-EHHHH