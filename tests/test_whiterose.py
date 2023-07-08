import unittest
from datetime import datetime
from unittest.mock import patch
from io import StringIO
from whiterose import localtime, today, Epoch


class TestWhiteRose(unittest.TestCase):
    def test_epoch_dump(self):
        result = Epoch.dump(2020, 12, 18, 16)
        expected = 1608328800.0
        self.assertEqual(result, expected)

    def test_epoch_dump_with_timezone(self):
        result = Epoch.dump(2020, 12, 18, 16, tz="Mexico/General")
        expected = 1608307200.0
        self.assertEqual(result, expected)

    def test_epoch_load(self):
        result = Epoch.load(1608328905.92277)
        expected = datetime(2020, 12, 18, 16, 1, 45)
        self.assertEqual(result, str(expected))


if __name__ == '__main__':
    unittest.main()
