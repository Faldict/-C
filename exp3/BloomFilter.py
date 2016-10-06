#!/usr/bin/env python
from Bitarray import Bitarray
from GeneralHashFunctions import RSHash, JSHash, PJWHash, BKDRHash

bit_map = Bitarray(32000)

def BloomFilter(s):
	h1 = RSHash(s)
	h2 = JSHash(s)
	h3 = PJWHash(s)
	h4 = BKDRHash(s)
	if bit_map.get(h1) and bit_map.get(h2) and bit_map.get(h3) and bit_get(h4):
		bit_map.set(h1)
		bit_map.set(h2)
		bit_map.set(h3)
		bit_map.set(h4)
		return True
	else:
		return False
