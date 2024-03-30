import unittest
import pytest

#class TestExample(unittest.TestCase):

@pytest.mark.usefixtures("setup")
class Test_sample:

    def test_example(self):
        mes = "hello"
        print(mes)

    def test_sums(self):
        print("IO will do sum")

    def test_subs(self):
        print("IO will do sub")

    def test_mults(self):
        print("IO will do mult")

