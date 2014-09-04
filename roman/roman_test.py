#!/usr/bin/env python

import unittest

from roman import romanize

class TestRomanNumber(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1_2_3(self):
        self.assertEquals('I', romanize(1))
        self.assertEquals('II', romanize(2))
        self.assertEquals('III', romanize(3))

    def test_4(self):
        self.assertEquals('IV', romanize(4))

    def test_5(self):
        self.assertEquals('V', romanize(5))

    def test_6_7_8(self):
        self.assertEquals('VI', romanize(6))
        self.assertEquals('VII', romanize(7))
        self.assertEquals('VIII', romanize(8))

    def test_9(self):
        self.assertEquals('IX', romanize(9))

    def test_10(self):
        self.assertEquals('X', romanize(10))

    def test_11_12_13(self):
        self.assertEquals('XI', romanize(11))
        self.assertEquals('XII', romanize(12))
        self.assertEquals('XIII', romanize(13))

    def test_10_to_100(self):
        self.assertEquals('XX', romanize(20))
        self.assertEquals('XL', romanize(40))
        self.assertEquals('LXX', romanize(70))
        self.assertEquals('XC', romanize(90))

    def test_10_to_100_with_1_to_9(self):
        self.assertEquals('XXXIII', romanize(33))
        self.assertEquals('XLIV', romanize(44))
        self.assertEquals('LXXVII', romanize(77))
        self.assertEquals('XCIX', romanize(99))

    def test_100_to_1000_with_low_symbols(self):
        self.assertEquals('CCCXXXIII', romanize(333))
        self.assertEquals('CDXLIV', romanize(444))
        self.assertEquals('DCCLXXVII', romanize(777))
        self.assertEquals('CMXCIX', romanize(999))

    def test_after_1000(self):
        self.assertEquals('MMMCCCXXXIII', romanize(3333))
        self.assertEquals('MMMCMXCIX', romanize(3999))
        ### are below values valid?
        self.assertEquals('MMMMCDXLIV', romanize(4444))
        self.assertEquals('MMMMMMMDCCLXXVII', romanize(7777))
        self.assertEquals('MMMMMMMMMCMXCIX', romanize(9999))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()