import unittest
from udun import main


class MainTest(unittest.TestCase):
    def test_main(self):
        args = []
        main(args)

    def test_version(self):
        args = ['--version']
        try:
            main(args)
        except SystemExit:
            pass
