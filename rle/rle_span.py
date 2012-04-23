#!/usr/bin/env python

class RLESpan:
	def __init__(self, key):
		self.key = key
		self.width = 1

	def increment(self):
		self.width += 1

	def widen(self):
		self.increment()

	def __repr__(self):
		return self.key * self.width

if __name__ == '__main__':
	rles = RLESpan("z")
	print rles

	rles.increment()
	rles.increment()
	rles.widen()
	rles.widen()
	print rles
