#!/usr/bin/env python

from spectrum import Spectrum
from byte_string import ByteString
from html_elements.cell import Cell
from html_elements.inline_style import InlineStyle

class HTMLSpectrum(Spectrum):
	def __init__(self, text, colour = None, size = None):
		Spectrum.__init__(self, text)
		self.colour = colour
		self.size = size

		self.make_spacer_line()
		self.construct()

	def make_spacer_line(self):
		spacer = ByteString("0")
		for i in self.text[1:]:
			spacer.add("0")
		spacer.do_not_compress()
		self.insert(0, spacer)

	def construct(self):
		ins = InlineStyle()
		ins.colour('transparent')
		self.table = "<!-- '%s' begins -->\n" % (self.text)
		self.table += '<table class="%s" cellpadding="%d" cellspacing="%d" style="%s">\n' % ('spectrum', 0, 0, str(ins))
		top_row = True
		for line in self:
			self.table += '<tr>'
			first_column = True
			for rel in line.compressed:
				c = Cell(rel.width, rel.key)
				if self.colour:
					c.set_colour(self.colour)
				if top_row and self.size:
					c.set_width("%spx" % (self.size))
				if first_column and self.size:
					c.set_height("%spx" % (self.size))
				self.table += str(c)
				first_column = False
			self.table += '</tr>\n'
			top_row = False
		self.table += '</table>\n'
		self.table += "<!-- '%s' ends -->" % (self.text)

	def __repr__(self):
		return self.table

if __name__ == '__main__':
	from colours import Colours
	from optparse import *
	usage = """Usage: %prog [options] <text>"""
	parser = OptionParser(usage = usage)
	parser.add_option(
			"-c", "--colour",
			action = 'store',
			dest = 'colour',
			help = "Foreground colour"
			)
	parser.add_option(
		"-x", "--hex-colour",
			action = 'store',
			dest = 'hex_colour',
			help = "Non-standard foreground colour as hex value"
			)
	parser.add_option(
			"-s", "--size",
			action = 'store',
			dest = 'size',
			help = "Size of the table cells"
			)
	options, args = parser.parse_args()
	if not options.size:
		options.size = 3
	if not options.colour:
		options.colour = "red"

	colours = Colours()
	colour = colours.get_hex(options.colour)
	if options.hex_colour:
		colour = "#%s" % (options.hex_colour)

	try:
		hs = HTMLSpectrum(
				args[0], 
				colour = colour,
				size = options.size 
				)
		print hs
	except IndexError:
		parser.print_usage()
		import sys
		sys.exit(1)
	
