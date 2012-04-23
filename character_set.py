#!/usr/bin/env python

class CharacterSet(dict):
	def __init__(self, charset_file = "conf/character_set.txt"):
		lines = open(charset_file).readlines()

		for line in lines:
			l = r'%s' % (line)
			bits = l.split("\t")
			self[bits[0]] = []
			for bit in bits[1].split(" "):
				self[bits[0]].append(int(bit.strip()))

	def __repr__(self):
		s = ""
		k = self.keys()
		k.sort()
		for j in k:
			s += j
			s += "\t"
			s += str(self[j])
			s += "\n"

		return s

if __name__ == '__main__':
	cs = CharacterSet()
	print (cs)

