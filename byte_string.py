#!/usr/bin/env python

from utils.padded_byte import PaddedByte
from rle.rle_string import RLEString

class ByteString:
	def __init__(self, octet):
		self.text = str(PaddedByte(octet))
		self.compress_me = True

	def add(self, octet):
		self.text += str(PaddedByte(octet))

	def do_not_compress(self):
		self.compress_me = False
		self.compress()

	def compress(self):
		self.compressed = RLEString(self.text, self.compress_me)

	def __repr__(self):
		return str(self.text)

if __name__ == '__main__':
	import sys
	bs = ByteString(sys.argv[1])
	bs.add(sys.argv[2])
	bs.compress()
	print bs
