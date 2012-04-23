#!/usr/bin/env python

from rle_span import RLESpan

class RLEString(list):
	def __init__(self, text, compressed = True):
		self.text = text
		self.compressed = compressed

		if self.compressed:
			self.compress()
		else:
			self.fake_compress()

	def compress(self):
		index = 0
		last_char = self.text[0]
		self.append(RLESpan(last_char))
		for char in self.text[1:]:
			if char == last_char:
				self[index].widen()
			else:
				self.append(RLESpan(char))
				index += 1

			last_char = char

	def fake_compress(self):
		for char in self.text:
			self.append(RLESpan(char))

if __name__ == '__main__':
	import sys
	rles = RLEString(sys.argv[1], False)
	print rles
