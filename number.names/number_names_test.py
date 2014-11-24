#!/usr/bin/env python

import unittest

from number_names import spell_number

class TestNumber2String(unittest.TestCase):
	def test_0(self):
		self.assertEqual('zero', spell_number(0))

	def test_one_digit(self):
		self.assertEqual('one', spell_number(1))
		self.assertEqual('three', spell_number(3))
		self.assertEqual('five', spell_number(5))
		self.assertEqual('seven', spell_number(7))
		self.assertEqual('nine', spell_number(9))

	def test_teens(self):
		self.assertEqual('ten', spell_number(10))
		self.assertEqual('eleven', spell_number(11))
		self.assertEqual('twelve', spell_number(12))
		self.assertEqual('thirteen', spell_number(13))
		self.assertEqual('nineteen', spell_number(19))

	def test_two_digits(self):
		self.assertEqual('twenty four', spell_number(24))
		self.assertEqual('thirty six', spell_number(36))
		self.assertEqual('fifty two', spell_number(52))
		self.assertEqual('ninety eight', spell_number(98))

	def test_three_digits(self):
		self.assertEqual('one hundred', spell_number(100))
		self.assertEqual('seven hundred and three', spell_number(703))
		self.assertEqual('two hundred and fourteen', spell_number(214))
		self.assertEqual('four hundred and sixteen', spell_number(416))
		self.assertEqual('three hundred and seventeen', spell_number(317))

	def test_pure_thousand(self):
		self.assertEqual('two thousand', spell_number(2000))
		self.assertEqual('ten thousand', spell_number(10000))
		self.assertEqual('eighteen thousand', spell_number(18000))
		self.assertEqual('one hundred and nine thousand', spell_number(109000))

	def test_thousand_follows_digits(self):
		self.assertEqual('three thousand, one hundred and two', spell_number(3102))
		self.assertEqual('fourteen thousand, five', spell_number(14005))
		self.assertEqual('one hundred and ten thousand, fifteen', spell_number(110015))

	def test_millions(self):
		self.assertEqual('one hundred and sixty three million, fourty five thousand, six hundred and seven', spell_number(163045607))

	def test_billions(self):
		self.assertEqual('nine hundred and eighty billion, seventy', spell_number(980000000070))

if __name__ == '__main__':
	unittest.main()
