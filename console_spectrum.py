#!/usr/bin/env python

from spectrum import Spectrum

class ConsoleSpectrum(Spectrum):
	def __init__(self, text, on_char = "O", off_char = " "):
		Spectrum.__init__(self, text)
		self.on_char = on_char
		self.off_char = off_char * len(self.on_char)

	def __repr__(self):
		import os
		terminal_width = int(os.popen('stty size', 'r').read().split()[1])
		offset = (terminal_width - (len(self.text) * len(self.on_char) * 8)) / 2
		s = ""
		for line in self:
			s += " " * offset
			s += str(line).replace("0", self.off_char).replace("1", self.on_char)
			s += '\n'

		return s

if __name__ == '__main__':
	from optparse import *
	usage = """Usage: %prog [options] <text>"""
	parser = OptionParser(usage = usage)
	parser.add_option(
			"-c", "--characters",
			action = "store",
			dest = "characters",
			help = "The characters to use"
			)
	options, args = parser.parse_args()

	if not options.characters:
		options.characters = "[]"
	try:
		cs = ConsoleSpectrum(args[0], options.characters)
		print cs
	except IndexError:
		parser.print_usage()
		import sys
		sys.exit(1)
