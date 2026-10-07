import unittest

import switchboard


class PackageTest(unittest.TestCase):
    def test_version(self):
        self.assertEqual(switchboard.__version__, "0.0.0")


if __name__ == "__main__":
    unittest.main()
