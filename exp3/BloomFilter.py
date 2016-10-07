#!/usr/bin/env python
from Bitarray import Bitarray
from GeneralHashFunctions import RSHash, JSHash, PJWHash, BKDRHash

class BloomFilter():
	def __init__(self, size):
		self.bit_map = Bitarray(size)

	def BloomFilter(self, s):
		h1 = RSHash(s)
		h2 = JSHash(s)
		h3 = PJWHash(s)
		h4 = BKDRHash(s)
		if not (self.bit_map.get(h1) and self.bit_map.get(h2) and self.bit_map.get(h3) and self.bit_map.get(h4)):
			self.bit_map.set(h1)
			self.bit_map.set(h2)
			self.bit_map.set(h3)
			self.bit_map.set(h4)
			return True
		else:
			return False
