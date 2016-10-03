#!/usr/bin/env python
from Bitarray import Bitarray

bit_map = Bitarray(32000)

def hash1(key):
	seed = 11
	hash = 0
	for i in range(len(key)):
		hash = hash * seed + Ord(key[i])
	return hash

def hash2(key):
	seed = 13
	hash = 0
	for i in range(len(key)):
		hash = hash * seed + Ord(key[i])
	return hash

def hash3(key):
	seed = 17
	hash = 0
	for i in range(len(key)):
		hash = hash * seed + Ord(key[i])
	return hash

def hash4(key):
	seed = 19
	hash = 0
	for i in range(len(key)):
		hash = hash * seed + Ord(key[i])
	return hash

def BloomFilter(s):
	h1 = hash1(s)
	h2 = hash2(s)
	h3 = hash3(s)
	h4 = hash4(s)
	if bit_map.get(h1) and bit_map.get(h2) and bit_map.get(h3) and bit_get(h4):
		bit_map.set(h1)
		bit_map.set(h2)
		bit_map.set(h3)
		bit_map.set(h4)
		return True
	else:
		return False
