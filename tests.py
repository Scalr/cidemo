import time
import unittest


class DemoTestCase(unittest.TestCase):
    def test_first(self):
        time.sleep(1)

    def test_second(self):
        time.sleep(1)

    def test_third(self):
        time.sleep(1)

    # def test_failed(self):
    #     raise AssertionError('Test failed!')
