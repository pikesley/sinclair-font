#!/usr/bin/env python

class CellClass:
	def __init__(self, boolean, blinken = False):
		if int(boolean) == 1:
			self.cls = "on"
		else:
			self.cls = "off"

		if blinken:
			self.cls = "blink" + self.cls

	def __repr__(self):
		return self.cls

if __name__ == '__main__':
	import sys

