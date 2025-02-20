import unittest
import os
from file_organizer.utils import ensure_dir_exists

class TestUtils(unittest.TestCase):
    def test_ensure_dir_exists(self):
        test_dir = "/tmp/test_dir"
        ensure_dir_exists(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        os.rmdir(test_dir)