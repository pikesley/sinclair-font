#!/usr/bin/env python

class PaddedByte:
	def __init__(self, octet):
		self.text = "%08d" % (int(bin(int(octet))[2:]))


	def __repr__(self):
		return self.text

if __name__ == '__main__':
	import sys
	pb = PaddedByte(int(sys.argv[1]))
	print pb
