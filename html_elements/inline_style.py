#!/usr/bin/env python

class InlineStyle(dict):
	def __init__(self, d = {}):
		for k in d.keys():
			self.add_style(k, d[k])

	def add_style(self, prop, val):
		if val:
			self[prop] = val

	def colour(self, colour):
		self.add_style('color', colour)

	def size(self, size):
		self.add_style('height', size)
		self.add_style('width', size)

	def contains_anything(self):
		return len(self.keys())

	def __repr__(self):
		if not self.keys():
			return ""
		s = ""
		for k in self.keys():
			s += k
			s += ": "
			s += self[k]
			s += "; "

		s = s.strip()
		return s

if __name__ == '__main__':
	ins = InlineStyle()
	print ins

	ins.colour("#000")
	ins.size("3px")
	ins.add_style("font-variant", "italic")

	print ins
