#!/usr/bin/env python

import yaml

class Colours(dict):
	def __init__(self, colour_file = "conf/colours.yaml"):
		f = open(colour_file, 'r')
		c = yaml.load(f)
		self.update(c)

	def get_hex(self, colour):
		try:
			return "#%s" % (self['hex'][colour])
		except KeyError:
			return "#%s" % (self['hex']['black'])

	def get_console(self, colour):
		try:
			return self['console'][colour]
		except KeyError:
			return self['console']['revert']

if __name__ == '__main__':
	c = Colours()
	print c

	print c.get_console("red") +  "foo" +  c.get_console('revert')
