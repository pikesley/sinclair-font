#!/usr/bin/env python

from cell_class import CellClass
from inline_style import InlineStyle

class Cell(dict):
	def __init__(self, colspan, boolean, blinken = False):
		self['colspan'] = colspan
		self['class'] = str(CellClass(boolean, blinken))
		self['style'] = InlineStyle()

	def set_colour(self, colour):
		if not self['class'] == 'off':
			self['style'].add_style('background-color', colour)

	def set_height(self, size):
		self['style'].add_style('height', size)

	def set_width(self, size):
		self['style'].add_style('width', size)

	def __repr__(self):
		s = '<td'

		for k in self.keys():
			if self[k]:
				s += " "
				s += k
				s += '="'
				s += str(self[k])
				s += '"'
	
		s += '></td>'

		return s

if __name__ == '__main__':
	c = Cell(1, 1)
	print c
	c = Cell(3, 0, True)
	print c

	c = Cell(4, 1)
	c.set_colour('#777')
	print c
	c = Cell(4, 0)
	c.set_colour('#777')
	print c
