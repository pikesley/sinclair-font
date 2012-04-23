#!/usr/bin/env python

from rle import *
from character_set import CharacterSet
from byte_string import ByteString

class Spectrum(list):
	def __init__(self, text):
		self.text = text
		self.cs = CharacterSet()

		self.assemble_chars()
		self.assemble_bytestrings()
		self.compress_bytestrings()

	def assemble_chars(self):
		self.char_list = []
		for c in self.text:
			self.char_list.append(self.cs[c])

	def assemble_bytestrings(self):
		for c in self.char_list:
			index = 0
			for octet in c:
				try:
					self[index].add(octet)
				except IndexError:
					self.append(ByteString(octet))
				index += 1

	def compress_bytestrings(self):
		for bs in self:
			bs.compress()

	def __repr__(self):
		s = ""
		for line in self:
			s += line.__repr__()
			s += '\n'

		return s

if __name__ == '__main__':
	import sys
	s = Spectrum(sys.argv[1])
	print s
